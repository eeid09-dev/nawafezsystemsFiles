#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Happy Fatora landing page - static multilingual SEO generator.

Usage:   python3 build.py https://your-real-domain.com [download-url]
Output:  ../site/index.html (ar) , ../site/en/index.html , ../site/fr/index.html
         + sitemap.xml, robots.txt, site.webmanifest, and og-source pages.
"""
import json, sys, os, html, urllib.parse, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'site')
DOMAIN = (sys.argv[1] if len(sys.argv) > 1 else 'https://www.happyfatora.com').rstrip('/')
DOWNLOAD_URL = sys.argv[2] if len(sys.argv) > 2 else ''          # app store link, when you have it
TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year

WA_INTL = '201004331221'          # wa.me format (no + , no spaces)
PHONE_EG = '01004331221'          # inside Egypt
PHONE_INT = '+201004331221'       # outside Egypt
CO_URL = 'https://www.nawafezsystems.com/'

LANGS = ['ar', 'en', 'fr']
IDX = {'ar': 0, 'en': 1, 'fr': 2}
DIR = {'ar': 'rtl', 'en': 'ltr', 'fr': 'ltr'}
LOCALE = {'ar': 'ar_EG', 'en': 'en_US', 'fr': 'fr_FR'}
LANG_NAME = {'ar': 'العربية', 'en': 'English', 'fr': 'Français'}
URL = {'ar': DOMAIN + '/', 'en': DOMAIN + '/en/', 'fr': DOMAIN + '/fr/'}

T = json.load(open(os.path.join(HERE, 'content.json'), encoding='utf-8'))

# ---------------------------------------------------------------- new / overridden copy  [ar, en, fr]
T.update({
 'seo_title': ["هابي فاتورة | برنامج فواتير ونقاط بيع ومخزون للمحلات",
               "Happy Fatora | POS, Invoicing & Inventory App for Shops",
               "Happy Fatora | Caisse POS, Facturation & Gestion de Stock"],
 'seo_desc': ["هابي فاتورة تطبيق فواتير ونقاط بيع (POS) وإدارة مخزون ومشتريات وعملاء وموردين. باركود، تقارير أرباح، طباعة حرارية، يعمل بدون إنترنت. ابدأ مجانًا.",
              "Happy Fatora is an invoicing, POS and inventory app for shops, supermarkets and pharmacies. Barcode, profit reports, thermal printing, offline use. Start free.",
              "Happy Fatora : facturation, caisse POS et gestion de stock pour commerces, supermarchés et pharmacies. Code-barres, rapports, mode hors ligne. Gratuit."],
 'seo_kw': ["هابي فاتورة, Happy Fatora, Happy Invoice, برنامج فواتير, برنامج محاسبة للمحلات, برنامج كاشير, نقاط البيع POS, برنامج إدارة المخزون, برنامج مبيعات ومشتريات, تطبيق فواتير للموبايل, برنامج فواتير مجاني, برنامج محاسبة بدون انترنت, برنامج سوبر ماركت, برنامج صيدلية, برنامج مطاعم وكافيهات, قارئ باركود, طباعة حرارية, إدارة العملاء والموردين, ديون العملاء, تقارير المبيعات والأرباح, ERP للشركات الصغيرة, برنامج فواتير اندرويد وايفون وويندوز, برنامج محاسبة في مصر",
            "Happy Fatora, Happy Invoice, invoicing app, POS app, point of sale software, inventory management app, barcode scanner app, small business accounting, offline POS, free invoice app, supermarket POS, pharmacy software, restaurant POS, customers and suppliers management, sales and purchases, thermal receipt printer, QR invoice, ERP for small business, Android iOS Windows POS, Arabic invoicing app, Egypt",
            "Happy Fatora, Happy Invoice, application de facturation, logiciel de caisse, point de vente POS, gestion de stock, lecteur code-barres, comptabilité petit commerce, caisse hors ligne, facturation gratuite, logiciel supermarché, logiciel pharmacie, logiciel restaurant, gestion clients et fournisseurs, imprimante thermique, facture QR, ERP pour PME, POS Android iOS Windows, application arabe de facturation"],
 'og_alt': ["هابي فاتورة: برنامج فواتير ونقاط بيع وإدارة مخزون للمحلات - واتساب 01004331221 - نوافذ سيستمز",
            "Happy Fatora: invoicing, POS and inventory app for shops - WhatsApp +201004331221 - Nawafez Systems",
            "Happy Fatora : facturation, caisse POS et gestion de stock pour commerces - WhatsApp +201004331221 - Nawafez Systems"],
 'wa_msg': ["مرحبًا، أريد الاستفسار عن تطبيق هابي فاتورة",
            "Hello, I would like to know more about the Happy Fatora app",
            "Bonjour, je souhaite en savoir plus sur l'application Happy Fatora"],
 'sub': ["هابي فاتورة برنامج فواتير ونقاط بيع (POS) لإدارة المحلات: المبيعات والمشتريات والمخزون والعملاء والموردين والتقارير، بتصميم عصري وسهل يناسب أي نشاط.",
         "Happy Fatora is an invoicing and POS app to run your shop: sales, purchases, inventory, customers, suppliers and reports, in a modern, easy design for any business.",
         "Happy Fatora est une application de facturation et de caisse (POS) pour gérer votre commerce : ventes, achats, stock, clients, fournisseurs et rapports, dans un design moderne et simple."],
 'rights': ["جميع الحقوق محفوظة لدى", "All rights reserved to", "Tous droits réservés à"],
 'n6': ["تواصل معنا", "Contact", "Contact"],
 'about_t': ["ما هو تطبيق هابي فاتورة؟", "What is Happy Fatora?", "Qu'est-ce que Happy Fatora ?"],
 'about_p1': ["هابي فاتورة (Happy Invoice) برنامج فواتير ومحاسبة ونقاط بيع (POS) متكامل لإدارة المحلات والشركات الصغيرة والمتوسطة من الموبايل أو الكمبيوتر. يغطي المبيعات والمشتريات والمخزون والعملاء والموردين والمرتجعات والمصروفات والديون في تطبيق واحد سهل بالعربية والإنجليزية والفرنسية.",
              "Happy Fatora (also known as Happy Invoice) is a complete invoicing, accounting and point-of-sale (POS) app for shops and small and medium businesses, on your phone or PC. It covers sales, purchases, inventory, customers, suppliers, returns, expenses and debts in one easy app available in Arabic, English and French.",
              "Happy Fatora (aussi appelée Happy Invoice) est une application complète de facturation, de comptabilité et de caisse (POS) pour les commerces et les PME, sur mobile ou PC. Elle gère ventes, achats, stock, clients, fournisseurs, retours, dépenses et dettes dans une seule application simple, en arabe, anglais et français."],
 'about_p2': ["يدعم قراءة وطباعة الباركود وQR، والطباعة الحرارية 58 و80 مم وطباعة A4، وتقارير الأرباح والضرائب والمخزون، والنسخ الاحتياطي. يعمل على أندرويد وآيفون وويندوز، ويعمل بدون إنترنت في الباقة المدفوعة.",
              "It supports barcode and QR scanning and printing, 58/80 mm thermal and A4 printing, profit, tax and stock reports, and backups. It runs on Android, iOS and Windows, and the paid plan works fully offline.",
              "Elle prend en charge la lecture et l'impression de codes-barres et QR, l'impression thermique 58/80 mm et A4, les rapports de bénéfices, de taxes et de stock, ainsi que les sauvegardes. Elle fonctionne sur Android, iOS et Windows, et l'offre payante fonctionne entièrement hors ligne."],
 'uses_t': ["مناسب لكل أنواع الأنشطة التجارية", "Built for every kind of business", "Adaptée à tous les types de commerces"],
 'ct_t': ["تواصل معنا", "Get in touch", "Contactez-nous"],
 'ct_s': ["اطلب الاشتراك أو اسأل عن أي ميزة، وسنرد عليك بسرعة على واتساب", "Ask about plans or any feature and we will reply quickly on WhatsApp", "Posez vos questions sur les offres ou les fonctionnalités, nous répondons vite sur WhatsApp"],
 'ct_eg': ["واتساب من داخل مصر", "WhatsApp from inside Egypt", "WhatsApp depuis l'Égypte"],
 'ct_int': ["واتساب من خارج مصر", "WhatsApp from outside Egypt", "WhatsApp depuis l'étranger"],
 'ct_co': ["الشركة المنتجة", "Producing company", "Société éditrice"],
 'co_full': ["نوافذ سيستمز .. لأنظمة البرمجيات", "Nawafez Systems – Software Systems", "Nawafez Systems – Systèmes logiciels"],
 'q5': ["هل يناسب السوبر ماركت والصيدليات والمطاعم؟", "Is it suitable for supermarkets, pharmacies and restaurants?", "Convient-elle aux supermarchés, pharmacies et restaurants ?"],
 'a5': ["نعم، يدعم الباركود وتواريخ الصلاحية والدفعات والوحدات المتعددة، فيناسب السوبر ماركت والصيدليات والمطاعم والكافيهات وتجار الجملة والمستودعات.",
        "Yes. With barcodes, expiry dates, batches and multiple units, it fits supermarkets, pharmacies, restaurants, cafés, wholesalers and warehouses.",
        "Oui. Grâce aux codes-barres, dates de péremption, lots et unités multiples, elle convient aux supermarchés, pharmacies, restaurants, cafés, grossistes et entrepôts."],
 'q6': ["ما أنظمة التشغيل المدعومة؟", "Which platforms are supported?", "Quelles plateformes sont prises en charge ?"],
 'a6': ["يعمل هابي فاتورة على أندرويد وآيفون (iOS) وويندوز.", "Happy Fatora runs on Android, iOS and Windows.", "Happy Fatora fonctionne sur Android, iOS et Windows."],
 'hero_alt': ["شاشة إنشاء فاتورة بيع في تطبيق هابي فاتورة", "Happy Fatora app screen: creating a sales invoice", "Écran de création d'une facture de vente dans Happy Fatora"],
 'steps_alt': ["لقطة شاشة ملخص النشاط في هابي فاتورة", "Happy Fatora business summary screenshot", "Capture du résumé d'activité dans Happy Fatora"],
 'a_menu': ["القائمة", "Menu", "Menu"], 'a_lang': ["اللغة", "Language", "Langue"], 'a_theme': ["تغيير المظهر", "Toggle theme", "Changer de thème"],
 'a_top': ["للأعلى", "Back to top", "Haut de page"], 'a_prev': ["السابق", "Previous", "Précédent"], 'a_next': ["التالي", "Next", "Suivant"],
 'a_wa': ["واتساب", "WhatsApp", "WhatsApp"], 'a_skip': ["تخطي إلى المحتوى", "Skip to content", "Aller au contenu"],
 'a_home': ["هابي فاتورة - الصفحة الرئيسية", "Happy Fatora - Home", "Happy Fatora - Accueil"],
 'call': ["اتصل", "Call", "Appeler"],
})


def tr(k, lang):
    return T[k][IDX[lang]]


def e(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- blocks
FEAT = [("bi-receipt", "f1"), ("bi-box-seam", "f2"), ("bi-people", "f3"), ("bi-cart-check", "f4"),
        ("bi-qr-code-scan", "f5"), ("bi-bar-chart-line", "f6"), ("bi-wallet2", "f7"), ("bi-palette", "f8")]
SHOTS = [("s-pos", "c1"), ("s-stock", "c2"), ("s-product", "c15"), ("s-qr", "c3"), ("s-barcode", "c13"), ("s-invoice", "c4"),
         ("s-invset", "c10"), ("s-reports", "c5"), ("s-cash", "c6"), ("s-expense", "c12"), ("s-customer", "c7"),
         ("s-supplier", "c11"), ("s-returns", "c16"), ("s-license", "c14"), ("s-lang", "c9"), ("s-menu", "c8")]
USES = [("bi-basket", "u1"), ("bi-capsule", "u2"), ("bi-cup-hot", "u3"), ("bi-truck", "u4"), ("bi-building", "u5"), ("bi-shop", "u6")]
SEC = [("bi-fingerprint", "k1"), ("bi-cloud-arrow-up", "k2"), ("bi-database-check", "k3"), ("bi-printer", "k4"), ("bi-currency-exchange", "k5"), ("bi-shield-lock", "k6")]
ROAD = [("bi-globe2", "r1"), ("bi-diagram-3", "r2"), ("bi-robot", "r3"), ("bi-person-gear", "r4")]
FAQ_N = 6


def blocks(L):
    t = lambda k: e(tr(k, L))
    b = {}
    b['feat'] = ''.join(
        f'<div class="col-sm-6 col-lg-3 rv"><article class="fcard"><div class="fi"><i class="bi {ic}" aria-hidden="true"></i></div><h3 class="h5 fw-bold">{t(k+"t")}</h3><p class="text-secondary mb-0">{t(k+"d")}</p></article></div>'
        for ic, k in FEAT)
    brand = tr('brand', L)
    b['gal'] = ''.join(
        f'<figure><div class="phone"><img loading="lazy" decoding="async" width="540" height="1200" src="{{{{root}}}}images/{f}.jpg" alt="{e(brand + " - " + tr(c, L))}"></div><figcaption>{t(c)}</figcaption></figure>'
        for f, c in SHOTS)
    b['steps'] = ''.join(
        f'<div class="step"><div class="num" aria-hidden="true">{i}</div><div><h3 class="h5 fw-bold mb-1">{t(f"h{i}t")}</h3><p class="text-secondary mb-0">{t(f"h{i}d")}</p></div></div>'
        for i in range(1, 5))
    b['faq'] = ''.join(
        f'<div class="accordion-item"><h3 class="accordion-header"><button class="accordion-button{"" if i == 1 else " collapsed"}" type="button" data-bs-toggle="collapse" data-bs-target="#a{i}" aria-expanded="{"true" if i == 1 else "false"}" aria-controls="a{i}">{t(f"q{i}")}</button></h3><div id="a{i}" class="accordion-collapse collapse{" show" if i == 1 else ""}" data-bs-parent="#faqList"><div class="accordion-body text-secondary">{t(f"a{i}")}</div></div></div>'
        for i in range(1, FAQ_N + 1))
    b['uses'] = ''.join(
        f'<li class="col-6 col-md-4"><div class="use" ><i class="bi {ic}" aria-hidden="true"></i><span>{t(k)}</span></div></li>'
        for ic, k in USES)
    # list items carry data-ic for the JS marquee
    b['uses'] = ''.join(
        f'<li class="col-6 col-md-4" data-ic="{ic}"><div class="use"><i class="bi {ic}" aria-hidden="true"></i><span>{t(k)}</span></div></li>'
        for ic, k in USES)
    b['sec'] = ''.join(
        f'<div class="col-md-6 col-lg-4 rv"><article class="kcard"><div class="fi"><i class="bi {ic}" aria-hidden="true"></i></div><div><h3 class="h5 fw-bold">{t(k+"t")}</h3><p class="text-secondary mb-0">{t(k+"d")}</p></div></article></div>'
        for ic, k in SEC)
    b['road'] = ''.join(
        f'<div class="col-sm-6 col-lg-3 rv"><article class="rm"><small>{t("soon")}</small><i class="bi {ic}" aria-hidden="true"></i><h3 class="h5 fw-bold mt-2">{t(k+"t")}</h3><p class="text-secondary mb-0">{t(k+"d")}</p></article></div>'
        for ic, k in ROAD)
    return b


# ---------------------------------------------------------------- structured data
def jsonld(L):
    i = IDX[L]
    url = URL[L]
    title, desc = tr('seo_title', L), tr('seo_desc', L)
    og = f"{DOMAIN}/images/og-{L}.jpg"
    org = {
        "@type": "Organization", "@id": DOMAIN + "/#publisher",
        "name": "Nawafez Systems", "alternateName": ["نوافذ سيستمز", "نوافذ سيستمز .. لأنظمة البرمجيات"],
        "url": CO_URL, "sameAs": [CO_URL],
        "contactPoint": [{"@type": "ContactPoint", "telephone": PHONE_INT, "contactType": "customer support",
                          "availableLanguage": ["Arabic", "English", "French"]}],
    }
    site = {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "Happy Fatora",
            "alternateName": ["هابي فاتورة", "Happy Invoice"], "inLanguage": ["ar", "en", "fr"], "publisher": {"@id": org["@id"]}}
    app = {
        "@type": "SoftwareApplication", "@id": url + "#app",
        "name": tr('brand', L), "alternateName": ["Happy Fatora", "Happy Invoice", "هابي فاتورة"],
        "description": tr('about_p1', L), "applicationCategory": "BusinessApplication",
        "applicationSubCategory": "POS, Invoicing, Inventory",
        "operatingSystem": "Android, iOS, Windows", "inLanguage": ["ar", "en", "fr"],
        "image": og, "url": url,
        "screenshot": [f"{DOMAIN}/images/{f}.jpg" for f, _ in SHOTS[:6]],
        "featureList": [tr(k + 't', L) for _, k in FEAT],
        "publisher": {"@id": org["@id"]}, "author": {"@id": org["@id"]},
        "offers": [
            {"@type": "Offer", "name": tr('pf', L), "price": "0", "priceCurrency": "USD", "url": url + "#pricing"},
            {"@type": "Offer", "name": tr('py', L), "price": "10", "priceCurrency": "USD", "url": url + "#pricing"},
            {"@type": "Offer", "name": tr('p3', L), "price": "25", "priceCurrency": "USD", "url": url + "#pricing"},
        ],
    }
    if DOWNLOAD_URL:
        app["downloadUrl"] = DOWNLOAD_URL
    page = {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "inLanguage": L,
            "isPartOf": {"@id": site["@id"]}, "about": {"@id": app["@id"]}, "dateModified": TODAY,
            "primaryImageOfPage": {"@type": "ImageObject", "url": og, "width": 1200, "height": 630}}
    faq = {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": L, "mainEntity": [
        {"@type": "Question", "name": tr(f'q{n}', L), "acceptedAnswer": {"@type": "Answer", "text": tr(f'a{n}', L)}}
        for n in range(1, FAQ_N + 1)]}
    return json.dumps({"@context": "https://schema.org", "@graph": [org, site, page, app, faq]}, ensure_ascii=False, separators=(',', ':'))


# ---------------------------------------------------------------- page template
PAGE = r'''<!DOCTYPE html>
<html lang="{{lang}}" dir="{{dir}}" data-bs-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{title}}</title>
<meta name="description" content="{{desc}}">
<meta name="keywords" content="{{kw}}">
<meta name="author" content="Nawafez Systems">
<meta name="publisher" content="Nawafez Systems">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="bingbot" content="index, follow">
<meta name="language" content="{{lang}}">
<meta name="application-name" content="Happy Fatora">
<meta name="apple-mobile-web-app-title" content="Happy Fatora">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#4CAF50" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0d1410" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<meta name="rating" content="general">
<meta name="geo.region" content="EG">
<meta name="geo.placename" content="Egypt">

<link rel="canonical" href="{{url}}">
{{alternates}}
<link rel="icon" href="{{root}}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{{root}}images/favicon-32.png">
<link rel="icon" type="image/png" sizes="48x48" href="{{root}}images/favicon-48.png">
<link rel="apple-touch-icon" sizes="180x180" href="{{root}}images/apple-touch-icon.png">
<link rel="manifest" href="{{abs}}/site.webmanifest">

<meta property="og:type" content="website">
<meta property="og:site_name" content="{{brand}}">
<meta property="og:title" content="{{title}}">
<meta property="og:description" content="{{desc}}">
<meta property="og:url" content="{{url}}">
<meta property="og:locale" content="{{locale}}">
{{og_alt_locales}}
<meta property="og:image" content="{{og}}">
<meta property="og:image:secure_url" content="{{og}}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{{og_alt}}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{title}}">
<meta name="twitter:description" content="{{desc}}">
<meta name="twitter:image" content="{{og}}">
<meta name="twitter:image:alt" content="{{og_alt}}">
<meta name="twitter:url" content="{{url}}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap{{bsrtl}}.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="{{root}}assets/site.css?v={{ver}}">
<script>try{var t=localStorage.getItem('theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.setAttribute('data-bs-theme',t)}catch(e){}</script>
<noscript><style>.rv{opacity:1!important;transform:none!important}</style></noscript>
<script type="application/ld+json">{{jsonld}}</script>
</head>
<body>
<a class="skip" href="#main">{{a_skip}}</a>
<div id="prog"></div>

<header>
<nav class="navbar navbar-expand-lg fixed-top" aria-label="Main">
  <div class="container">
    <a class="navbar-brand d-flex align-items-center gap-2 fw-bold" href="#top" aria-label="{{a_home}}">
      <span class="brand-logo"><img src="{{root}}images/logo.png" width="42" height="42" alt="{{brand}}"></span><span>{{brand}}</span>
    </a>
    <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#nav" aria-controls="nav" aria-expanded="false" aria-label="{{a_menu}}"><i class="bi bi-list fs-2" aria-hidden="true"></i></button>
    <div class="collapse navbar-collapse" id="nav">
      <ul class="navbar-nav mx-auto">
        <li class="nav-item"><a class="nav-link" href="#features">{{n1}}</a></li>
        <li class="nav-item"><a class="nav-link" href="#screens">{{n2}}</a></li>
        <li class="nav-item"><a class="nav-link" href="#how">{{n3}}</a></li>
        <li class="nav-item"><a class="nav-link" href="#pricing">{{n4}}</a></li>
        <li class="nav-item"><a class="nav-link" href="#faq">{{n5}}</a></li>
        <li class="nav-item"><a class="nav-link" href="#contact">{{n6}}</a></li>
      </ul>
      <div class="d-flex align-items-center gap-2 py-2 py-lg-0">
        <div class="dropdown">
          <button class="icon-btn px-3 w-auto gap-2" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-label="{{a_lang}}"><i class="bi bi-translate" aria-hidden="true"></i><span class="fw-bold">{{LANGCODE}}</span></button>
          <ul class="dropdown-menu dropdown-menu-end">{{langmenu}}</ul>
        </div>
        <button class="icon-btn" id="themeBtn" type="button" aria-label="{{a_theme}}"><i class="bi bi-moon-stars" aria-hidden="true"></i></button>
        <a class="btn btn-g d-none d-sm-inline-block" href="{{dl}}"><i class="bi bi-download me-1" aria-hidden="true"></i>{{dl_t}}</a>
      </div>
    </div>
  </div>
</nav>
</header>

<main id="main">
<section class="hero" id="top">
  <span class="blob b1"></span><span class="blob b2"></span>
  <div class="container position-relative">
    <div class="row align-items-center g-5">
      <div class="col-lg-6 text-center text-lg-start">
        <span class="badge-soft mb-3"><i class="bi bi-stars" aria-hidden="true"></i><span>{{badge}}</span></span>
        <h1 class="mb-3">{{t1}} <span class="gt">{{t2}}</span></h1>
        <p class="lead text-secondary mb-4">{{sub}}</p>
        <div class="d-flex flex-wrap gap-3 justify-content-center justify-content-lg-start mb-5">
          <a class="btn btn-g btn-lg" href="{{dl}}"><i class="bi bi-download me-2" aria-hidden="true"></i>{{dl_t}}</a>
          <a class="btn btn-wa btn-lg" href="{{wa}}" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2" aria-hidden="true"></i>{{wa_t}}</a>
        </div>
        <p class="plat text-secondary mb-4 justify-content-lg-start"><span><i class="bi bi-android2" aria-hidden="true"></i>Android</span><span><i class="bi bi-apple" aria-hidden="true"></i>iOS</span><span><i class="bi bi-windows" aria-hidden="true"></i>Windows</span></p>
        <div class="row text-center g-3">
          <div class="col-4 stat"><b data-count="17" data-suf="+">17+</b><div class="small text-secondary">{{s1}}</div></div>
          <div class="col-4 stat"><b data-count="3">3</b><div class="small text-secondary">{{s2}}</div></div>
          <div class="col-4 stat"><b data-count="150" data-suf="+">150+</b><div class="small text-secondary">{{s3}}</div></div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="stage" id="stage">
          <div class="phone" id="heroPhone"><img src="{{root}}images/s-sales.jpg" width="540" height="1200" fetchpriority="high" decoding="async" alt="{{hero_alt}}"></div>
          <div class="chip c1"><i class="bi bi-check2-circle" aria-hidden="true"></i><span>{{chip1}}</span></div>
          <div class="chip c3"><i class="bi bi-upc-scan" aria-hidden="true"></i><span>{{chip3}}</span></div>
          <div class="chip c2"><i class="bi bi-graph-up-arrow" aria-hidden="true"></i><span>1,550 EGP</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="mq" aria-hidden="true"><div class="mq-track" id="mq"></div></div>

<section class="sec alt" id="about" aria-labelledby="about-h">
  <div class="container">
    <div class="text-center mb-4 rv"><h2 id="about-h">{{about_t}}</h2></div>
    <p class="about-p text-center rv">{{about_p1}}</p>
    <p class="about-p text-center mb-5 rv">{{about_p2}}</p>
    <h3 class="h4 fw-bold text-center mb-4 rv">{{uses_t}}</h3>
    <ul class="use-list row g-3 justify-content-center" id="useList">{{uses}}</ul>
  </div>
</section>

<section class="sec" id="features" aria-labelledby="features-h">
  <div class="container">
    <div class="text-center mb-5 rv"><h2 id="features-h">{{ft}}</h2><p class="text-secondary">{{fs}}</p></div>
    <div class="row g-4">{{feat}}</div>
  </div>
</section>

<section class="band" aria-label="{{brand}}"><div class="container"><div class="row g-4 text-center">
  <div class="col-6 col-md-3"><b data-count="150" data-suf="+">150+</b><span>{{sl1}}</span></div>
  <div class="col-6 col-md-3"><b data-count="3">3</b><span>{{sl2}}</span></div>
  <div class="col-6 col-md-3"><b data-count="17" data-suf="+">17+</b><span>{{sl3}}</span></div>
  <div class="col-6 col-md-3"><b data-count="3">3</b><span>{{sl4}}</span></div>
</div></div></section>

<section class="sec alt" id="screens" aria-labelledby="screens-h">
  <div class="container">
    <div class="text-center mb-3 rv"><h2 id="screens-h">{{sct}}</h2><p class="text-secondary">{{scs}}</p></div>
    <div class="d-flex justify-content-end gap-2 mb-2">
      <button class="icon-btn" id="gPrev" type="button" aria-label="{{a_prev}}"><i class="bi bi-chevron-left" aria-hidden="true"></i></button>
      <button class="icon-btn" id="gNext" type="button" aria-label="{{a_next}}"><i class="bi bi-chevron-right" aria-hidden="true"></i></button>
    </div>
    <div class="gal" id="gal">{{gal}}</div>
  </div>
</section>

<section class="sec" id="how" aria-labelledby="how-h">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6 rv"><div class="stage" style="max-width:280px"><div class="phone"><img src="{{root}}images/s-summary.jpg" width="540" height="1200" loading="lazy" decoding="async" alt="{{steps_alt}}"></div></div></div>
      <div class="col-lg-6 rv">
        <h2 class="mb-2" id="how-h">{{ht}}</h2><p class="text-secondary mb-4">{{hs}}</p>
        {{steps}}
      </div>
    </div>
  </div>
</section>

<section class="sec alt" id="security" aria-labelledby="security-h">
  <div class="container">
    <div class="text-center mb-5 rv"><h2 id="security-h">{{kt}}</h2><p class="text-secondary">{{ks}}</p></div>
    <div class="row g-4">{{sec}}</div>
  </div>
</section>

<section class="sec" id="pricing" aria-labelledby="pricing-h">
  <div class="container">
    <div class="text-center mb-5 rv"><h2 id="pricing-h">{{pt}}</h2><p class="text-secondary">{{ps}}</p></div>
    <div class="row g-4 justify-content-center">
      <div class="col-md-6 col-lg-4 rv"><div class="price">
        <h3 class="h4">{{pf}}</h3><p class="text-secondary">{{pfd}}</p>
        <div class="amt mb-3">{{free}}</div>
        <ul><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pb1}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pb2}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pb3}}</span></li></ul>
        <a class="btn btn-outline-success w-100 mt-3" href="{{dl}}">{{pbtn}}</a>
      </div></div>
      <div class="col-md-6 col-lg-4 rv"><div class="price">
        <h3 class="h4">{{py}}</h3><p class="text-secondary">{{pyd}}</p>
        <div class="amt mb-3">$10 <small class="fs-6 text-secondary">{{yr}}</small></div>
        <ul><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp1}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp2}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp3}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp4}}</span></li></ul>
        <a class="btn btn-g w-100 mt-3" href="{{wa}}" target="_blank" rel="noopener">{{psub}}</a>
      </div></div>
      <div class="col-md-6 col-lg-4 rv"><div class="price pop"><span class="tag">{{pop}}</span>
        <h3 class="h4">{{p3}}</h3><p class="text-secondary">{{p3d}}</p>
        <div class="amt mb-3">$25 <s class="fs-6 text-secondary">$30</s> <small class="fs-6 text-secondary">{{y3}}</small></div>
        <ul><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp1}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp2}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp3}}</span></li><li><i class="bi bi-check-circle-fill" aria-hidden="true"></i><span>{{pp4}}</span></li></ul>
        <a class="btn w-100 mt-3 text-white" style="background:var(--o)" href="{{wa}}" target="_blank" rel="noopener">{{psub}}</a>
      </div></div>
    </div>
  </div>
</section>

<section class="sec alt" id="roadmap" aria-labelledby="roadmap-h">
  <div class="container">
    <div class="text-center mb-5 rv"><h2 id="roadmap-h">{{rt}}</h2><p class="text-secondary">{{rs}}</p></div>
    <div class="row g-4">{{road}}</div>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-h">
  <div class="container" style="max-width:820px">
    <div class="text-center mb-5 rv"><h2 id="faq-h">{{qt}}</h2></div>
    <div class="accordion rv" id="faqList">{{faq}}</div>
  </div>
</section>

<section class="sec alt" id="contact" aria-labelledby="contact-h">
  <div class="container">
    <div class="text-center mb-5 rv"><h2 id="contact-h">{{ct_t}}</h2><p class="text-secondary">{{ct_s}}</p></div>
    <div class="row g-4 justify-content-center">
      <div class="col-md-6 col-lg-4 rv"><div class="ccard">
        <div class="fi"><i class="bi bi-whatsapp" aria-hidden="true"></i></div>
        <h3 class="h5 fw-bold">{{ct_eg}}</h3>
        <a class="num-link my-2" href="{{wa}}" target="_blank" rel="noopener">{{phone_eg}}</a>
        <div><a class="btn btn-wa mt-2" href="{{wa}}" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2" aria-hidden="true"></i>{{wa_t}}</a></div>
      </div></div>
      <div class="col-md-6 col-lg-4 rv"><div class="ccard">
        <div class="fi"><i class="bi bi-globe-americas" aria-hidden="true"></i></div>
        <h3 class="h5 fw-bold">{{ct_int}}</h3>
        <a class="num-link my-2" href="{{wa}}" target="_blank" rel="noopener">{{phone_int}}</a>
        <div><a class="btn btn-wa mt-2" href="{{wa}}" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2" aria-hidden="true"></i>{{wa_t}}</a></div>
      </div></div>
      <div class="col-md-6 col-lg-4 rv"><div class="ccard">
        <div class="fi"><i class="bi bi-building" aria-hidden="true"></i></div>
        <h3 class="h5 fw-bold">{{ct_co}}</h3>
        <p class="my-2 fw-bold">{{co_full}}</p>
        <a class="btn btn-g mt-2" href="{{co_url}}" target="_blank" rel="noopener" title="{{co_full}}"><i class="bi bi-box-arrow-up-right me-2" aria-hidden="true"></i>nawafezsystems.com</a>
      </div></div>
    </div>
  </div>
</section>

<section class="pb-5 pt-5">
  <div class="container"><div class="cta rv">
    <h2 class="fw-bold mb-2 position-relative">{{ct}}</h2>
    <p class="mb-4 opacity-75 position-relative">{{cs}}</p>
    <div class="d-flex flex-wrap gap-3 justify-content-center position-relative">
      <a class="btn btn-light btn-lg" href="{{dl}}"><i class="bi bi-download me-2" aria-hidden="true"></i>{{dl_t}}</a>
      <a class="btn btn-wa btn-lg" href="{{wa}}" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2" aria-hidden="true"></i>{{wa_t}}</a>
    </div>
  </div></div>
</section>
</main>

<footer>
  <div class="container">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-center gap-3 text-center">
      <div class="d-flex align-items-center gap-2 fw-bold"><span class="logo" style="width:36px;height:36px"><img src="{{root}}images/logo.png" width="36" height="36" loading="lazy" alt="{{brand}}"></span><span>{{brand}}</span><span class="text-secondary fw-normal d-none d-md-inline">— {{tag}}</span></div>
      <div class="text-secondary">© {{year}} {{rights}} <a href="{{co_url}}" target="_blank" rel="noopener" title="{{co_full}}">{{co_full}}</a></div>
    </div>
    <div class="d-flex flex-wrap justify-content-center gap-3 mt-3 small text-secondary text-center">
      <span>{{ct_eg}}: <a class="tel" href="{{wa}}" target="_blank" rel="noopener">{{phone_eg}}</a></span>
      <span>{{ct_int}}: <a class="tel" href="tel:{{phone_int}}">{{phone_int}}</a></span>
    </div>
    <nav class="flinks text-center mt-3 small" aria-label="Languages">{{footlangs}}</nav>
  </div>
</footer>

<button id="top2" type="button" aria-label="{{a_top}}"><i class="bi bi-arrow-up" aria-hidden="true"></i></button>
<a class="wa" href="{{wa}}" target="_blank" rel="noopener" aria-label="{{a_wa}} {{phone_int}}"><i class="bi bi-whatsapp" aria-hidden="true"></i></a>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer></script>
<script src="{{root}}assets/site.js?v={{ver}}" defer></script>
</body>
</html>
'''


def rel_url(frm, to):
    """relative link between language folders"""
    if frm == to:
        return './' if frm == 'ar' else './'
    base = {'ar': '', 'en': 'en/', 'fr': 'fr/'}
    if frm == 'ar':
        return base[to]
    return '../' + base[to]


def render(L):
    i = IDX[L]
    root = '' if L == 'ar' else '../'
    t = lambda k: e(tr(k, L))
    wa = f"https://wa.me/{WA_INTL}?text={urllib.parse.quote(tr('wa_msg', L))}"
    dl = DOWNLOAD_URL or '#contact'
    alternates = ''.join(f'<link rel="alternate" hreflang="{x}" href="{URL[x]}">\n' for x in LANGS)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{URL["ar"]}">'
    og_alt_locales = '\n'.join(f'<meta property="og:locale:alternate" content="{LOCALE[x]}">' for x in LANGS if x != L)
    langmenu = ''.join(
        f'<li><a class="dropdown-item{" active" if x == L else ""}" href="{rel_url(L, x)}" hreflang="{x}" lang="{x}"{" aria-current=true" if x == L else ""}>{LANG_NAME[x]}</a></li>' for x in LANGS)
    footlangs = ' | '.join(f'<a href="{rel_url(L, x)}" hreflang="{x}" lang="{x}">{LANG_NAME[x]}</a>' for x in LANGS)
    b = blocks(L)

    # simple keys that map 1:1 to translated text
    skip_keys = set()
    simple = {k: t(k) for k in T}
    ctx = dict(simple)
    ctx.update({
        'lang': L, 'dir': DIR[L], 'root': root, 'abs': DOMAIN, 'bsrtl': '.rtl' if L == 'ar' else '',
        'title': t('seo_title'), 'desc': t('seo_desc'), 'kw': t('seo_kw'), 'url': URL[L], 'locale': LOCALE[L],
        'og': f'{DOMAIN}/images/og-{L}.jpg', 'og_alt': t('seo_title') and e(tr('og_alt', L)),
        'og_alt_locales': og_alt_locales, 'alternates': alternates, 'jsonld': jsonld(L).replace('</', '<\\/'),
        'brand': t('brand'), 'LANGCODE': L.upper(), 'langmenu': langmenu, 'footlangs': footlangs,
        'wa': wa, 'dl': dl, 'dl_t': t('dl'), 'wa_t': t('wa'),
        'phone_eg': PHONE_EG, 'phone_int': PHONE_INT, 'co_url': CO_URL, 'year': str(YEAR), 'ver': TODAY.replace('-', ''),
        'feat': b['feat'], 'gal': b['gal'].replace('{{root}}', root), 'steps': b['steps'], 'faq': b['faq'],
        'uses': b['uses'], 'sec': b['sec'], 'road': b['road'],
    })
    out = PAGE
    # replace longest keys first to avoid partial overlaps
    for k in sorted(ctx, key=len, reverse=True):
        out = out.replace('{{' + k + '}}', ctx[k])
    assert '{{' not in out, [s for s in out.split('{{')[1:3]]
    return out


def og_html(L):
    """1200x630 social share image source (Cairo via Google Fonts when online)."""
    rtl = L == 'ar'
    tx = lambda k: e(tr(k, L))
    chips = {
        'ar': ['فواتير', 'نقاط بيع POS', 'مخزون', 'باركود', 'تقارير'],
        'en': ['Invoices', 'POS', 'Inventory', 'Barcode', 'Reports'],
        'fr': ['Factures', 'Caisse POS', 'Stock', 'Code-barres', 'Rapports'],
    }[L]
    head = {'ar': 'برنامج فواتير ونقاط بيع ومخزون', 'en': 'Invoicing, POS & Inventory App', 'fr': 'Facturation, Caisse POS & Stock'}[L]
    sub = {'ar': 'كل محلك في جيبك.. بدون إنترنت', 'en': 'Your whole shop in your pocket', 'fr': 'Toute votre boutique dans la poche'}[L]
    lab_eg = {'ar': 'واتساب من داخل مصر', 'en': 'WhatsApp - inside Egypt', 'fr': 'WhatsApp - Égypte'}[L]
    lab_int = {'ar': 'من خارج مصر', 'en': 'Outside Egypt', 'fr': "Depuis l'étranger"}[L]
    by = {'ar': 'تطوير', 'en': 'By', 'fr': 'Par'}[L]
    co_og = tr('co_full', L) if rtl else 'Nawafez Systems'
    wa_svg = '<svg width="34" height="34" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#25D366"/><path fill="#fff" d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1.02l-2.2 2.2z" transform="translate(3 3) scale(.75)"/></svg>'
    chip_html = ''.join(f'<span class="chip">{e(c)}</span>' for c in chips)
    return f'''<!DOCTYPE html>
<html lang="{L}" dir="{DIR[L]}"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1200px;height:630px;overflow:hidden}}
body{{font-family:'Cairo','DejaVu Sans',sans-serif;color:#fff;position:relative;
 background:radial-gradient(circle at 12% 8%,rgba(255,152,0,.35),transparent 38%),radial-gradient(circle at 92% 95%,rgba(155,225,93,.35),transparent 40%),linear-gradient(135deg,#124d17 0%,#1f6f28 45%,#2e8b34 100%)}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(rgba(255,255,255,.10) 2px,transparent 2px) 0 0/34px 34px}}
.wrap{{position:absolute;inset:0;display:flex;flex-direction:row-reverse}}
.phones{{position:relative;width:470px;flex:none}}
.ph{{position:absolute;width:262px;border-radius:34px;border:8px solid #0b0f0c;background:#0b0f0c;overflow:hidden;box-shadow:0 30px 60px -18px rgba(0,0,0,.65)}}
.ph img{{display:block;width:100%;height:auto}}
.p1{{top:60px;{'left' if rtl else 'right'}:150px;transform:rotate({-6 if rtl else 6}deg);z-index:2}}
.p2{{top:130px;{'left' if rtl else 'right'}:-10px;transform:rotate({7 if rtl else -7}deg);opacity:.96}}
.txt{{flex:1;padding:46px {'0 0 56px' if rtl else '56px 0 0'};padding:46px 56px 0 56px;display:flex;flex-direction:column}}
.brand{{display:flex;align-items:center;gap:16px;margin-bottom:6px}}
.brand img{{width:76px;height:76px;border-radius:20px;box-shadow:0 10px 24px -8px rgba(0,0,0,.5)}}
.name{{font-size:{76 if rtl else 62}px;font-weight:900;line-height:1.15;white-space:nowrap;letter-spacing:{0 if rtl else -1}px}}
.head{{font-size:{36 if rtl else 31}px;white-space:nowrap;font-weight:800;line-height:1.35;color:#ffd27a;margin-top:6px}}
.sub{{font-size:27px;font-weight:600;opacity:.92;margin-top:4px}}
.chips{{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}}
.chip{{padding:5px 14px;border-radius:99px;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.35);font-weight:700;font-size:19px}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:128px;z-index:10;background:#0a2a0e;border-top:2px solid rgba(255,255,255,.18);display:flex;align-items:center;justify-content:space-between;padding:0 56px;flex-direction:{'row' if rtl else 'row'}}}
.contact{{display:flex;gap:34px;align-items:center}}
.c{{display:flex;align-items:center;gap:12px}}
.c small{{display:block;font-size:17px;opacity:.8;font-weight:600;line-height:1.2}}
.c b{{display:block;font-size:31px;font-weight:800;direction:ltr;unicode-bidi:isolate;line-height:1.2;letter-spacing:.5px}}
.co{{text-align:{'left' if rtl else 'right'}}}
.co small{{font-size:16px;opacity:.8;font-weight:600;display:block}}
.co b{{font-size:25px;font-weight:800;display:block;line-height:1.3;color:#ffd27a}}
.co span{{font-size:19px;font-weight:600;direction:ltr;unicode-bidi:isolate;display:inline-block;opacity:.95}}
</style></head>
<body><div class="wrap">
 <div class="phones"><div class="ph p2"><img src="../../site/images/s-stock.jpg"></div><div class="ph p1"><img src="../../site/images/s-pos.jpg"></div></div>
 <div class="txt">
  <div class="brand"><img src="../../site/images/logo-green.png"><div class="name">{tx('brand')}</div></div>
  <div class="head">{e(head)}</div>
  <div class="sub">{e(sub)}</div>
  <div class="chips">{chip_html}</div>
 </div>
 <div class="bar">
  <div class="contact">
   <div class="c">{wa_svg}<div><small>{e(lab_eg)}</small><b>{PHONE_EG}</b></div></div>
   <div class="c"><div><small>{e(lab_int)}</small><b>{PHONE_INT}</b></div></div>
  </div>
  <div class="co"><small>{e(by)}</small><b style="white-space:nowrap">{e(co_og)}</b><span>www.nawafezsystems.com</span></div>
 </div>
</div></body></html>'''


def write(path, data):
    path = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(data)


def main():
    for L in LANGS:
        page = render(L)
        write('index.html' if L == 'ar' else f'{L}/index.html', page)
        t_, d_ = tr('seo_title', L), tr('seo_desc', L)
        print(f'{L}: title {len(t_)} chars, description {len(d_)} chars')
        os.makedirs(os.path.join(HERE, 'og'), exist_ok=True)
        open(os.path.join(HERE, 'og', f'og-{L}.html'), 'w', encoding='utf-8').write(og_html(L))

    # sitemap with hreflang alternates + images
    alts = ''.join(f'    <xhtml:link rel="alternate" hreflang="{x}" href="{URL[x]}"/>\n' for x in LANGS)
    alts += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{URL["ar"]}"/>\n'
    urls = ''.join(f'''  <url>
    <loc>{URL[L]}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{"1.0" if L == "ar" else "0.9"}</priority>
{alts}    <image:image><image:loc>{DOMAIN}/images/og-{L}.jpg</image:loc><image:title>{e(tr("seo_title", L))}</image:title></image:image>
  </url>
''' for L in LANGS)
    write('sitemap.xml', f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
{urls}</urlset>
''')
    write('robots.txt', f'''User-agent: *
Allow: /

# Social preview crawlers
User-agent: facebookexternalhit
Allow: /
User-agent: Twitterbot
Allow: /
User-agent: WhatsApp
Allow: /
User-agent: LinkedInBot
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
''')
    write('site.webmanifest', json.dumps({
        "name": "هابي فاتورة | Happy Fatora", "short_name": "Happy Fatora", "description": tr('seo_desc', 'ar'),
        "start_url": "/", "scope": "/", "display": "standalone", "lang": "ar", "dir": "rtl",
        "background_color": "#ffffff", "theme_color": "#4CAF50",
        "icons": [{"src": "/images/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
                  {"src": "/images/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]
    }, ensure_ascii=False, indent=2))
    print('domain:', DOMAIN, '| download url:', DOWNLOAD_URL or '(none -> buttons scroll to #contact)')


main()
