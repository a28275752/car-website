from flask import Flask, render_template

app = Flask(__name__)

#首頁路由
@app.route("/")
def home():
    return render_template("index.html")

# 商品資料
products = [
    {"name": "不死圖騰", "price": 9999, "image": "https://zh.minecraft.wiki/images/Totem_of_Undying_JE2_BE2.png?bec78"},
    {"name": "難道說貓貓", "price": 420, "image": "https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.15752-9/494336493_1212870799703225_5535772275244109255_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=9f807c&_nc_ohc=YTtOTX8riQgQ7kNvwEZuL_i&_nc_oc=AdnV_Yoj51tx5b_5jYhw7PWjrtXN_Uxew2OK7kfKHs856ol4Dx12fmO0SiARWJbrKV0&_nc_zt=23&_nc_ht=scontent.fkhh1-2.fna&oh=03_Q7cD2QERUoSA3Pf51phr3chi2rTYIn6lhD3n6vb1_naxV0kd5w&oe=68426655"},
    {"name": "耄耋", "price": 580, "image": "https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.15752-9/494815994_1252443493558273_4679079484192809457_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=9f807c&_nc_ohc=Kl7nhxTZLrAQ7kNvwFcTAf-&_nc_oc=AdmkRk77bYBzwMOCvUBM7q_C7vqxgnS8iU8MKMyL9WY-GtACTs1cfGbevImtbgw0A1c&_nc_zt=23&_nc_ht=scontent.fkhh1-1.fna&oh=03_Q7cD2QGwVFm9Agb6lmZBZJzjm0RYsYckO-QJMvSBF5ZKQ2372g&oe=68427E44"},
    {"name": "Driver cat", "price": 9999, "image": "https://truth.bahamut.com.tw/s01/202408/621d64188954368b2440bc4cc51afe85.JPG"},
    {"name": "huh cat", "price": 9999, "image": "https://truth.bahamut.com.tw/s01/202408/7fc06df8131801af714af81327b76493.PNG"},
    {"name": "震驚哈基咪", "price": 9999, "image": "https://truth.bahamut.com.tw/s01/202408/da6940230f3dd66b0cfe2be10e841eac.PNG"},
    {"name": "nice", "price": 9999, "image": "https://truth.bahamut.com.tw/s01/202408/a5917397f8132d77b8f195c8f3f22ec7.PNG"},
    {"name": "oi", "price": 9999, "image": "https://cdn.fbsbx.com/v/t59.2708-21/484149843_657537353296556_1179091541932141811_n.gif?_nc_cat=108&_nc_cb=47395efc-a3eb5992&ccb=1-7&_nc_sid=cf94fc&_nc_ohc=KYrpLegaJVkQ7kNvwHSULI5&_nc_oc=AdmXOBafCKVL4wyOt8ZKre2WerPcNgcYMY0KJhIQFGJt1pM4KXPn9ZMhH5xKkgbyNAU&_nc_zt=7&_nc_ht=cdn.fbsbx.com&_nc_gid=vJIAUAszuKMgImHUmpF_cg&oh=03_Q7cD2QHP9YOpTVXlTpxVDJaftMa8swbxweujD0OTxOwnWoELYw&oe=681D2367"},
    {"name": "嘲笑貓", "price": 9999, "image": "https://truth.bahamut.com.tw/s01/202408/forum/60076/667bb92826a64df46ec139b904ce312e.JPG"},


]

#產品介紹路由
@app.route("/products")
def product_page():
    return render_template("products.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)