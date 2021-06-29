# checkstat
Grepping for URLs according to the status code

# Descripiton
This is a simple tool that allows you to get the responses of different requests in a easy way. You can search for specific status codes and save the output as well. 

# Installation
`git clone https://github.com/kavishkagihan/checkstat.git`

`cd checkstat`

`chmod +x checkstat.py`


# Adding the script to path
If you are willing to use this tool from any place without using the absolute path, you will have to add this directory to your path
`sudo echo "PATH=$PATH:/path/to/the/script" > ~/.bashrc`

# Usage
You can get the help menu with `./checkstat.py -h `
![image](https://user-images.githubusercontent.com/85458014/123797613-e665d880-d8d5-11eb-8d42-164a0e916f78.png)


The most simple usage would be to get the responses of a given url list. By default this will read from stdin, but you can specify a file if you want.

`./checkstat.py -f url_list`

![image](https://user-images.githubusercontent.com/85458014/123794611-8c174880-d8d2-11eb-9e74-a078060301b5.png)

If you look closely, it is using http protocol instead of https. You can force it to use https with `-p` option.

![image](https://user-images.githubusercontent.com/85458014/123794792-cb459980-d8d2-11eb-9351-2511e47c6b51.png)

If you have a big list of URLs and you want this to done quickly, you can increase the threads with `-t` option.
And If you want to save the results of this, you can use `-I` options including `-H` and `-B`. However if you want to save the results, you will have specify a output directory with `-o` option.
`./checkstat.py -f hosts -p -I -H -B -o output_directory`

`-H` stands for the headers and `-B` stands for the body. So it will save the headers of the response in .header file and the body in .body file.
.header file
![image](https://user-images.githubusercontent.com/85458014/123796227-6db24c80-d8d4-11eb-8f9b-b6817c6b2065.png)

.body file
![image](https://user-images.githubusercontent.com/85458014/123796255-760a8780-d8d4-11eb-8d48-c818e24455a1.png)

Also if you want to use multiple tools with a same command, you can get the input from stdin.
`echo google.com|./checkstat.py -p`

Lastly, the most important usage would be to grep for specific status codes. You can do it with `-s`.
`cat hosts|./checkstat.py -s 404 -p`

![image](https://user-images.githubusercontent.com/85458014/123796841-15c81580-d8d5-11eb-8c54-2aa3be623706.png)

# Contact
Find me, instagram - @_kavi.gihan, email - iamkavigihan@gmail.com







