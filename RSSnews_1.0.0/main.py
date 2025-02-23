import tkinter as tk
import feedparser

# 新闻源配置
news_sources = {
    "百度": {
        "热搜": "https://rss.aishort.top/?type=baidu",
        "国内": "https://news.baidu.com/n?cmd=4&class=civilnews&tn=rss",
        "国际": "https://news.baidu.com/n?cmd=1&class=internews&tn=rss",
        "军事": "http://news.baidu.com/n?cmd=4&class=mil&tn=rss",
        "财经": "http://news.baidu.com/n?cmd=4&class=finannews&tn=rss",
        "房产": "http://news.baidu.com/n?cmd=4&class=housenews&tn=rss",
        "汽车": "https://news.baidu.com/n?cmd=4&class=autonews&tn=rss",
        "体育": "https://news.baidu.com/n?cmd=4&class=sportnews&tn=rss",
        "娱乐": "http://news.baidu.com/n?cmd=4&class=enternews&tn=rss",
        "游戏": "https://news.baidu.com/n?cmd=4&class=gamenews&tn=rss",
        "教育": "https://news.baidu.com/n?cmd=4&class=edunews&tn=rss",
        "女性": "https://news.baidu.com/n?cmd=4&class=healthnews&tn=rss",
        "科技": "https://news.baidu.com/n?cmd=4&class=technnews&tn=rss",
        "社会": "http://news.baidu.com/n?cmd=4&class=socianews&tn=rss"
    },
    "中国新闻网": {
        "即时": "https://www.chinanews.com.cn/rss/scroll-news.xml",
        "焦点": "https://www.chinanews.com.cn/rss/importnews.xml",
        "政治": "https://www.chinanews.com.cn/rss/china.xml",
        "国际": "https://www.chinanews.com.cn/rss/world.xml",
        "社会": "https://www.chinanews.com.cn/rss/society.xml",
        "财经": "https://www.chinanews.com.cn/rss/finance.xml",
        "文娱": "https://www.chinanews.com.cn/rss/culture.xml",
        "体育": "https://www.chinanews.com.cn/rss/sports.xml"
    },
    "更多": {
        "IT之家": "https://www.ithome.com/rss/",
        "Nvidia": "https://blogs.nvidia.com/feed/",
        "ScienceNet": "https://www.sciencenet.cn/xml/news-0.aspx?news=0"
    }
}

# 新闻获取函数
def get_news(RSS_source):
    text.delete(1.0, tk.END)
    feed = feedparser.parse(RSS_source)
    for i, entry in enumerate(feed.entries, start=1):
        news = f"{i}. {entry.title}\n{entry.link}\n{entry.published}\n"
        text.insert(tk.END, news)

# 创建菜单项
def create_menu(menu, category, items):
    submenu = tk.Menu(menu, tearoff=0)
    for label, url in items.items():
        submenu.add_command(label=label, command=lambda u=url: get_news(u))
    menu.add_cascade(label=category, menu=submenu)

# 创建主窗口
root = tk.Tk()
root.title("News")
root.geometry("550x720")
root.config(bg="gray")
root.resizable(False, False)

# 创建菜单栏
menu_bar = tk.Menu(root)
for category, items in news_sources.items():
    create_menu(menu_bar, category, items)
menu_bar.add_command(label="退出", command=root.quit)
root.config(menu=menu_bar)

# 创建滚动文本框
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(root, yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT, fill=tk.BOTH)
text.config(font=("微软雅黑", 12), bg="white")
scrollbar.config(command=text.yview)

# 运行窗口
root.mainloop()