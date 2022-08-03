# check-breach
Checks If Password Ever Been Breached Via HaveIBeenPwned APIv3 Without Sending Original Password. Use Any One Of Them.

## Why This?
1. It's Easiar Then Web Inferface. CLI Is Always Better.
2. I Don't Need To Share My Password With [HaveIBeenPwned](https://haveibeenpwned.com/) Site.
3. It Usage **[K-Anonymity Model](https://en.wikipedia.org/wiki/K-anonymity)** Which Allow Leaked Password Searching Without Disclosing The Real Password.
4. Make You Realize That You Need A Password Manager Right Now!

## Example
**With Python**
```bash
python check-breach.py <YOUR_PASSWORD>

python check-breach.py P@$$Od123
```

**With Bash**
```bash
chmod +x check-breach

./check-breach P@$$Od123
```

# License
MIT License
Copyright (c) 2022 FlareXes
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
