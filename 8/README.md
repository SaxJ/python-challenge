# Challenge 8
* Viewing page source, there's a link mapped in the image, that prompts for
  username and password. The source has a username and password encoded in some
  way. The prompt says "inflate", so I must need to do that to get the username
  and password.
* Tried zlib and gzip and neither worked. Used linux `file` utility on the
  username string to conclude that it is bzipped
* Decompressing the string gives un: 'huge', pw: 'file'
* Whoa, already on to 9
