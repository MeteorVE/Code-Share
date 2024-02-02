Almost all links are saved in these ``.txt`` files.
Some of these pages require to login to access.

# Origins

I want to clone the whole website for offline viewing.
To be honest, there were many difficulties that made me want to give up.  Many times.

But I still did it --- although there are still some flaws.
For example, the js animation doesn't always work properly, many parts have to be handled manually, and custom code is required for different categories.



![](https://s.meteorv.dev/amitafcclone)

# Tips

- The skills you need: **Python**, **Selenium**, some of **Front-End knowledge**.
  - Start doing it with your keyboard than slowly reading a textbook to learn, and learn faster.
- Extract image-links / css-links / js-links
  - Decide filename -> download -> replace link to path of file.
  - Use ``urlparse`` (``urllib.parse``) to determine if the domain is same as the main page.
- Some manual download
  - The image-links in css-file (background-image)
    - Hint: search ``/assets/maeshimaami`` in css file.
  - Movies.
    - ``video-downloader-for-vime`` is a good plugin for Chrome.
  - Some elements such as favicon or others ... Especially on the home page.
    - ``Save All Resources``(plugin) may do this --- but I just use it for comparison.
- In Gallery, the image is present by "background-image" style.
  - So you need to replace text in inline-style.
    - read style as ``String`` and replace with ``regex``.
- In Gallery, source image link is hidden.
  - Replace the links in ``data-original``.
- If url contains ``?page=2``, replace it.
  - E.g. ``https://maeshima-ami.jp/products?page=2`` -> ``https://maeshima-ami.jp/products/page/2``
  - We can **read** the former, and **save** it under the latter's name(path).
- **Load cookie** to access credential pages.
  - You need to get cookie manually of course. 
  - I don't think that log in **EVERYTIMES** is a good solution. Careful to be banned.
- About wallpaper
  - I have consolidated all the wallpaper links and their corresponding file names. 
    You can download them yourself using ``wgets`` or ``requests``. 
    Of course, this also requires cookies.
  - In ``wallpaper.csv``
- About download files(images, js, css ... etc)
  - Recommend: Use my ``download-module.py``.
    This help you to check if file exist and make sure directory has been created.
- Some files/urls contain japanese.
  - Use ``parse.unquote(filename)`` to get correct path.





# Keywords

> In order to allow others to search for this article. 
> Instead of using these keywords to accomplish.

website-clone

site-clone

website-crawler

Website-Cloner

https://maeshima-ami.jp/

前島亜美



# Contact

G-mail: ekids12345@gmail.com

Or using this repo to open issue.

Feel free to ask me --- before 2023/03/01. (Official site closing time.)

> 2023年3月1日(水)以降は当サイトにアクセスできなくなります。
