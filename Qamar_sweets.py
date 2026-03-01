from flask import Flask, render_template_string

app = Flask(__name__)

# ضع روابط حساباتك هنا لتعمل الأزرار بشكل صحيح
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61555271198225"
INSTAGRAM_URL = "https://www.instagram.com/qamar_sweets_39/?__pwa=1" # استبدل your_username بحسابك

INDEX_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>حلويات قمر | فخامة المذاق</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Cairo:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: 'Cairo', sans-serif; scroll-behavior: smooth; background-color: #fffafb; }
        .brand-font { font-family: 'Amiri', serif; }
        .glass-nav { background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(219, 39, 119, 0.1); }
        .hero-bg {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1535141192574-5d4897c12636?auto=format&fit=crop&w=1350&q=80');
            background-size: cover; background-position: center; background-attachment: fixed;
        }
        .reveal { transition: all 0.8s ease-out; opacity: 0; transform: translateY(25px); }
        .reveal.active { opacity: 1; transform: translateY(0); }
        
        /* تأثيرات الأزرار */
        .btn-contact { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
        .btn-contact:hover { transform: translateY(-5px) scale(1.05); }
        
        .fb-btn { background: #1877F2; box-shadow: 0 10px 20px -5px rgba(24, 119, 242, 0.4); }
        .ig-btn { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); box-shadow: 0 10px 20px -5px rgba(220, 39, 67, 0.4); }
    </style>
</head>
<body>

    <nav class="fixed w-full z-50 glass-nav">
        <div class="max-w-7xl mx-auto px-6 py-5 flex justify-between items-center">
            <div class="text-3xl font-bold text-pink-600 brand-font">قمر <span class="text-pink-400">للحلى</span></div>
            <div class="hidden md:flex space-x-10 space-x-reverse font-bold text-gray-700">
                <a href="#home" class="hover:text-pink-600 transition">الرئيسية</a>
                <a href="#gallery" class="hover:text-pink-600 transition">أعمالنا</a>
                <a href="#contact" class="hover:text-pink-600 transition">اطلب الآن</a>
            </div>
        </div>
    </nav>

    <section id="home" class="hero-bg h-screen flex items-center justify-center text-center text-white">
        <div class="max-w-4xl px-4 reveal active">
            <h1 class="text-6xl md:text-8xl font-bold mb-6 brand-font leading-tight">حلويات قمر <br><span class="text-pink-400">تليق بمناسباتكم</span></h1>
            <p class="text-xl md:text-2xl mb-12 opacity-90 font-light">نحن لا نصنع الكيك فقط، بل نصنع ذكريات لا تُنسى.</p>
            <div class="flex flex-wrap justify-center gap-6">
                <a href="#contact" class="bg-pink-600 hover:bg-pink-700 text-white px-12 py-5 rounded-full font-bold text-lg shadow-2xl transition-all">اطلب عبر التواصل الاجتماعي</a>
            </div>
        </div>
    </section>

    <section id="gallery" class="py-32 max-w-7xl mx-auto px-6">
        <div class="text-center mb-20 reveal">
            <h2 class="text-5xl font-bold text-slate-900 brand-font">معرض الإبداع</h2>
            <div class="h-1.5 w-24 bg-pink-500 mx-auto mt-4 rounded-full"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-10">
            <div class="rounded-[2.5rem] overflow-hidden shadow-xl reveal border-4 border-white"><img src="https://scontent.fogx1-1.fna.fbcdn.net/v/t39.30808-6/627176756_122282794730175706_6783747790280727454_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=7b2446&_nc_ohc=XKovgakYDecQ7kNvwHteX3N&_nc_oc=Adn6hm71BGSTMxTYabUo0qTnSMNILNXNbW_47gSHPndGpp23BHJ5JzdtIUskknBgwwA&_nc_zt=23&_nc_ht=scontent.fogx1-1.fna&_nc_gid=iNpgJ7yNzHIsT2tGllzgwg&_nc_ss=8&oh=00_AfuMOUPgWsxhwAvDq8837kutcCfvVZLeIVOyC3lcROJIEw&oe=69AA6DE7" class="w-full h-96 object-cover hover:scale-110 transition duration-700"></div>
            <div class="rounded-[2.5rem] overflow-hidden shadow-xl reveal border-4 border-white" style="transition-delay: 150ms;"><img src="https://scontent.fogx1-1.fna.fbcdn.net/v/t39.30808-6/641712054_122286125558175706_1738809769325179804_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=7b2446&_nc_ohc=BnkR_QQd7lsQ7kNvwHxDm8F&_nc_oc=Adm5u1SBTw1Spf3BfxSsXBk1bmyWTleyiYT-X9mEmMaljJZD7U1vJUizRL166QfT5MA&_nc_zt=23&_nc_ht=scontent.fogx1-1.fna&_nc_gid=LbGnf131cFa5iqFEJaldOQ&_nc_ss=8&oh=00_AfuDqLz8sSv0gxBw_uJJUQAjCAxwUS2btOAUV410x2L1-w&oe=69AA593B" class="w-full h-96 object-cover hover:scale-110 transition duration-700"></div>
            <div class="rounded-[2.5rem] overflow-hidden shadow-xl reveal border-4 border-white" style="transition-delay: 300ms;"><img src="https://scontent.fogx1-1.fna.fbcdn.net/v/t39.30808-6/628033726_122282794454175706_5105740860786148994_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=7b2446&_nc_ohc=aqRXVf7ihpEQ7kNvwE6Xho7&_nc_oc=AdnbXVrpJan14c3bJGt7oL6Tvm9YoHI-lH-JdZmW21im0l6RKocn7Q2RVaNfGMhLLww&_nc_zt=23&_nc_ht=scontent.fogx1-1.fna&_nc_gid=A6eDYzIGK3gBHA3bEuVM6Q&_nc_ss=8&oh=00_AfuF7vMvuFpsGImPabKjsffy5tOWUggdPsQess2NaNFG_Q&oe=69AA808F" class="w-full h-96 object-cover hover:scale-110 transition duration-700"></div>
        </div>
    </section>

    <section id="contact" class="py-32 bg-pink-100/30">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <div class="bg-white p-16 rounded-[4rem] shadow-2xl border border-pink-100 reveal">
                <h2 class="text-4xl font-bold text-slate-800 mb-6 brand-font italic">لطلب كيكتكم الخاصة..</h2>
                <p class="text-gray-500 text-lg mb-12 leading-relaxed">يسعدنا استقبال طلباتكم واستفساراتكم مباشرة عبر منصات التواصل الاجتماعي. اضغط على المنصة المفضل لديك:</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <a href="{{fb}}" target="_blank" class="btn-contact fb-btn text-white py-6 rounded-3xl flex items-center justify-center gap-4 text-xl font-bold">
                        <i class="fab fa-facebook-f text-3xl"></i>
                        راسلنا على فيسبوك
                    </a>
                    
                    <a href="{{ig}}" target="_blank" class="btn-contact ig-btn text-white py-6 rounded-3xl flex items-center justify-center gap-4 text-xl font-bold">
                        <i class="fab fa-instagram text-3xl"></i>
                        تابعنا على إنستغرام
                    </a>
                    <h3 class="text-2xl font-bold text-gray-700 mt-8 md:mt-0">أو اتصل بنا مباشرة على <span class="text-pink-600">06.99.11.99.11</span></h3>
                </div>
                
                <p class="mt-12 text-sm text-gray-400 font-medium tracking-wide italic">نحن متواجدون للرد عليكم طوال أيام الأسبوع</p>
            </div>
        </div>
    </section>

    <footer class="py-16 text-center text-gray-400">
        <div class="text-2xl font-bold text-pink-600 brand-font mb-4">حلويات قمر</div>
        <p class="text-sm italic">© 2026 جميع الحقوق محفوظة</p>
    </footer>

    <script>
        function reveal() {
            var reveals = document.querySelectorAll(".reveal");
            for (var i = 0; i < reveals.length; i++) {
                var windowHeight = window.innerHeight;
                var elementTop = reveals[i].getBoundingClientRect().top;
                if (elementTop < windowHeight - 100) { reveals[i].classList.add("active"); }
            }
        }
        window.addEventListener("scroll", reveal); reveal();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(INDEX_HTML, fb=FACEBOOK_URL, ig=INSTAGRAM_URL)

if __name__ == '__main__':
    app.run(port=5000, debug=True)