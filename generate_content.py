#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate full privacy-policy JSON for every PlatePrivacy app locale."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"

# Filename key → language (Belarusian file is by.json, key is "by")
LANGS = [
    "en", "ru", "uk", "by", "de", "fr", "es", "it", "pt", "nl", "pl", "cs", "sk",
    "hu", "ro", "bg", "el", "tr", "sv", "da", "nb", "fi", "et", "lv", "lt", "hr",
    "sl", "sr_Latn", "bs", "mk", "sq", "is", "ca", "ga", "mt", "zh_CN", "ja", "ko", "vi",
]

APPODEAL = (
    '<a href="https://www.appodeal.com/privacy-policy" rel="noopener">'
    "Appodeal Privacy Policy</a>"
)
APPODEAL_RU = (
    '<a href="https://www.appodeal.com/privacy-policy" rel="noopener">'
    "Политику конфиденциальности Appodeal</a>"
)
APPODEAL_UK = (
    '<a href="https://www.appodeal.com/privacy-policy" rel="noopener">'
    "Політику конфіденційності Appodeal</a>"
)
MAIL = '<a href="mailto:pavelpalityka@gmail.com">pavelpalityka@gmail.com</a>'
GPLAY = (
    '<a href="https://payments.google.com/payments/apis-secure/'
    'get_legal_document?ldl=en_GB&amp;ldo=0&amp;ldt=buyertos" rel="noopener">'
    "Google Play Terms</a>"
)


def L(**kwargs: str) -> dict[str, str]:
    """Build a dict for all langs; missing keys fall back to English.
    Pass Icelandic as is_= (is is a Python keyword).
    """
    if "is_" in kwargs:
        kwargs["is"] = kwargs.pop("is_")
    en = kwargs["en"]
    out = {k: en for k in LANGS}
    out.update(kwargs)
    if "by" not in kwargs and "ru" in kwargs:
        out["by"] = kwargs["ru"]
    return out


# --- Shared strings ---

TITLE = L(
    en="Privacy Policy — PlatePrivacy",
    ru="Политика конфиденциальности — PlatePrivacy",
    uk="Політика конфіденційності — PlatePrivacy",
    by="Палітыка прыватнасці — PlatePrivacy",
    de="Datenschutzerklärung — PlatePrivacy",
    fr="Politique de confidentialité — PlatePrivacy",
    es="Política de privacidad — PlatePrivacy",
    it="Informativa sulla privacy — PlatePrivacy",
    pt="Política de privacidade — PlatePrivacy",
    nl="Privacybeleid — PlatePrivacy",
    pl="Polityka prywatności — PlatePrivacy",
    cs="Zásady ochrany osobních údajů — PlatePrivacy",
    sk="Zásady ochrany osobných údajov — PlatePrivacy",
    hu="Adatvédelmi irányelvek — PlatePrivacy",
    ro="Politica de confidențialitate — PlatePrivacy",
    bg="Политика за поверителност — PlatePrivacy",
    el="Πολιτική απορρήτου — PlatePrivacy",
    tr="Gizlilik Politikası — PlatePrivacy",
    sv="Integritetspolicy — PlatePrivacy",
    da="Privatlivspolitik — PlatePrivacy",
    nb="Personvernerklæring — PlatePrivacy",
    fi="Tietosuojakäytäntö — PlatePrivacy",
    et="Privaatsuspoliitika — PlatePrivacy",
    lv="Privātuma politika — PlatePrivacy",
    lt="Privatumo politika — PlatePrivacy",
    hr="Pravila privatnosti — PlatePrivacy",
    sl="Pravilnik o zasebnosti — PlatePrivacy",
    sr_Latn="Politika privatnosti — PlatePrivacy",
    bs="Politika privatnosti — PlatePrivacy",
    mk="Политика за приватност — PlatePrivacy",
    sq="Politika e privatësisë — PlatePrivacy",
    is_="Persónuverndarstefna — PlatePrivacy",
    ca="Política de privadesa — PlatePrivacy",
    ga="Polasaí príobháideachais — PlatePrivacy",
    mt="Politika tal-privatezza — PlatePrivacy",
    zh_CN="隐私政策 — PlatePrivacy",
    ja="プライバシーポリシー — PlatePrivacy",
    ko="개인정보 처리방침 — PlatePrivacy",
    vi="Chính sách quyền riêng tư — PlatePrivacy",
)

UPDATED = L(
    en="Last updated: 8 September 2026",
    ru="Последнее обновление: 8 сентября 2026 г.",
    uk="Останнє оновлення: 8 вересня 2026 р.",
    by="Апошняе абнаўленне: 8 верасня 2026 г.",
    de="Zuletzt aktualisiert: 8. September 2026",
    fr="Dernière mise à jour : 8 septembre 2026",
    es="Última actualización: 8 de septiembre de 2026",
    it="Ultimo aggiornamento: 8 settembre 2026",
    pt="Última atualização: 8 de septiembre de 2026",
    nl="Laatst bijgewerkt: 8 september 2026",
    pl="Ostatnia aktualizacja: 8 września 2026",
    cs="Poslední aktualizace: 26. srpna 2026",
    sk="Posledná aktualizácia: 26. augusta 2026",
    hu="Utolsó frissítés: 2026. augusztus 26.",
    ro="Ultima actualizare: 26 august 2026",
    bg="Последна актуализация: 26 август 2026 г.",
    el="Τελευταία ενημέρωση: 26 Αυγούστου 2026",
    tr="Son güncelleme: 26 Ağustos 2026",
    sv="Senast uppdaterad: 26 augusti 2026",
    da="Senest opdateret: 26. august 2026",
    nb="Sist oppdatert: 26. august 2026",
    fi="Viimeksi päivitetty: 26. elokuuta 2026",
    et="Viimati uuendatud: 26. august 2026",
    lv="Pēdējoreiz atjaunināts: 2026. gada 26. augustā",
    lt="Paskutinį kartą atnaujinta: 2026 m. rugpjūčio 26 d.",
    hr="Zadnja ažuriranja: 26. kolovoza 2026.",
    sl="Zadnja posodobitev: 26. avgust 2026",
    sr_Latn="Poslednje ažuriranje: 26. avgust 2026.",
    bs="Posljednje ažuriranje: 26. august 2026.",
    mk="Последно ажурирање: 26 август 2026",
    sq="Përditësuar së fundi: 26 gusht 2026",
    is_="Síðast uppfært: 26. ágúst 2026",
    ca="Darrera actualització: 26 d’agost de 2026",
    ga="Nuashonraithe go deireanach: 26 Lúnasa 2026",
    mt="Aġġornat l-aħħar: 26 ta’ Awwissu 2026",
    zh_CN="最后更新：2026年8月26日",
    ja="最終更新：2026年8月26日",
    ko="최종 업데이트: 2026년 8월 26일",
    vi="Cập nhật lần cuối: 26 tháng 8 năm 2026",
)

FOOTER = L(
    en="© 2026 Pavel Palityka · PlatePrivacy",
    ru="© 2026 Павел Палитка · PlatePrivacy",
    uk="© 2026 Pavel Palityka · PlatePrivacy",
    by="© 2026 Павел Палітка · PlatePrivacy",
    de="© 2026 Pavel Palityka · PlatePrivacy",
    fr="© 2026 Pavel Palityka · PlatePrivacy",
    es="© 2026 Pavel Palityka · PlatePrivacy",
    it="© 2026 Pavel Palityka · PlatePrivacy",
    pt="© 2026 Pavel Palityka · PlatePrivacy",
    nl="© 2026 Pavel Palityka · PlatePrivacy",
    pl="© 2026 Pavel Palityka · PlatePrivacy",
    cs="© 2026 Pavel Palityka · PlatePrivacy",
    sk="© 2026 Pavel Palityka · PlatePrivacy",
    hu="© 2026 Pavel Palityka · PlatePrivacy",
    ro="© 2026 Pavel Palityka · PlatePrivacy",
    bg="© 2026 Pavel Palityka · PlatePrivacy",
    el="© 2026 Pavel Palityka · PlatePrivacy",
    tr="© 2026 Pavel Palityka · PlatePrivacy",
    sv="© 2026 Pavel Palityka · PlatePrivacy",
    da="© 2026 Pavel Palityka · PlatePrivacy",
    nb="© 2026 Pavel Palityka · PlatePrivacy",
    fi="© 2026 Pavel Palityka · PlatePrivacy",
    et="© 2026 Pavel Palityka · PlatePrivacy",
    lv="© 2026 Pavel Palityka · PlatePrivacy",
    lt="© 2026 Pavel Palityka · PlatePrivacy",
    hr="© 2026 Pavel Palityka · PlatePrivacy",
    sl="© 2026 Pavel Palityka · PlatePrivacy",
    sr_Latn="© 2026 Pavel Palityka · PlatePrivacy",
    bs="© 2026 Pavel Palityka · PlatePrivacy",
    mk="© 2026 Pavel Palityka · PlatePrivacy",
    sq="© 2026 Pavel Palityka · PlatePrivacy",
    is_="© 2026 Pavel Palityka · PlatePrivacy",
    ca="© 2026 Pavel Palityka · PlatePrivacy",
    ga="© 2026 Pavel Palityka · PlatePrivacy",
    mt="© 2026 Pavel Palityka · PlatePrivacy",
    zh_CN="© 2026 Pavel Palityka · PlatePrivacy",
    ja="© 2026 Pavel Palityka · PlatePrivacy",
    ko="© 2026 Pavel Palityka · PlatePrivacy",
    vi="© 2026 Pavel Palityka · PlatePrivacy",
)


def t(lang: str, d: dict[str, str]) -> str:
    return d.get(lang) or d["en"]


def build(lang: str) -> dict:
    """Assemble a complete policy document for one language."""
    # Section titles
    s_intro = t(lang, L(
        en="Introduction", ru="Введение", uk="Вступ", by="Уводзіны",
        de="Einführung", fr="Introduction", es="Introducción", it="Introduzione",
        pt="Introdução", nl="Inleiding", pl="Wprowadzenie", cs="Úvod", sk="Úvod",
        hu="Bevezetés", ro="Introducere", bg="Въведение", el="Εισαγωγή", tr="Giriş",
        sv="Inledning", da="Introduktion", nb="Innledning", fi="Johdanto", et="Sissejuhatus",
        lv="Ievads", lt="Įvadas", hr="Uvod", sl="Uvod", sr_Latn="Uvod", bs="Uvod",
        mk="Вовед", sq="Hyrje", is_="Inngangur", ca="Introducció", ga="Réamhrá", mt="Introduzzjoni",
        zh_CN="简介", ja="はじめに", ko="소개", vi="Giới thiệu",
    ))
    s_ctrl = t(lang, L(
        en="Data controller", ru="Оператор данных", uk="Контролер даних", by="Аператар даных",
        de="Verantwortlicher", fr="Responsable du traitement", es="Responsable del tratamiento",
        it="Titolare del trattamento", pt="Responsável pelo tratamento", nl="Verwerkingsverantwoordelijke",
        pl="Administrator danych", cs="Správce údajů", sk="Prevádzkovateľ", hu="Adatkezelő",
        ro="Operator de date", bg="Администратор на данни", el="Υπεύθυνος επεξεργασίας",
        tr="Veri sorumlusu", sv="Personuppgiftsansvarig", da="Dataansvarlig", nb="Behandlingsansvarlig",
        fi="Rekisterinpitäjä", et="Vastutav töötleja", lv="Datu pārzinis", lt="Duomenų valdytojas",
        hr="Voditelj obrade", sl="Upravljavec", sr_Latn="Rukovalac podacima", bs="Rukovalac podacima",
        mk="Контролор на податоци", sq="Kontrolluesi i të dhënave", is_="Ábyrgðaraðili",
        ca="Responsable del tractament", ga="Rialaitheoir sonraí", mt="Kontrollur tad-dejta",
        zh_CN="数据控制者", ja="データ管理者", ko="데이터 관리자", vi="Đơn vị kiểm soát dữ liệu",
    ))
    s_info = t(lang, L(
        en="Information processed by the app",
        ru="Какие данные обрабатывает приложение",
        uk="Які дані обробляє застосунок",
        by="Якія даныя апрацоўвае праграма",
        de="Informationen, die die App verarbeitet",
        fr="Informations traitées par l’application",
        es="Información que procesa la aplicación",
        it="Informazioni elaborate dall’app",
        pt="Informações processadas pela aplicação",
        nl="Gegevens die de app verwerkt",
        pl="Informacje przetwarzane przez aplikację",
        cs="Údaje zpracovávané aplikací",
        sk="Údaje spracúvané aplikáciou",
        hu="Az alkalmazás által kezelt adatok",
        ro="Informații prelucrate de aplicație",
        bg="Информация, обработвана от приложението",
        el="Πληροφορίες που επεξεργάζεται η εφαρμογή",
        tr="Uygulamanın işlediği bilgiler",
        sv="Information som appen behandlar",
        da="Oplysninger, som appen behandler",
        nb="Informasjon appen behandler",
        fi="Sovelluksen käsittelemät tiedot",
        et="Rakenduse töödeldav teave",
        lv="Informācija, ko apstrādā lietotne",
        lt="Programėlės tvarkoma informacija",
        hr="Podaci koje obrađuje aplikacija",
        sl="Podatki, ki jih obdeluje aplikacija",
        sr_Latn="Podaci koje obrađuje aplikacija",
        bs="Podaci koje obrađuje aplikacija",
        mk="Информации што ги обработува апликацијата",
        sq="Informacioni i përpunuar nga aplikacioni",
        is_="Upplýsingar sem appið vinnur",
        ca="Informació que processa l’aplicació",
        ga="Faisnéis a phróiseálann an aip",
        mt="Informazzjoni pproċessata mill-app",
        zh_CN="应用处理的信息",
        ja="アプリが処理する情報",
        ko="앱이 처리하는 정보",
        vi="Thông tin ứng dụng xử lý",
    ))
    s_perm = t(lang, L(
        en="Android permissions", ru="Разрешения Android", uk="Дозволи Android", by="Дазволы Android",
        de="Android-Berechtigungen", fr="Autorisations Android", es="Permisos de Android",
        it="Autorizzazioni Android", pt="Permissões Android", nl="Android-machtigingen",
        pl="Uprawnienia Android", cs="Oprávnění Android", sk="Povolenia Android",
        hu="Android-engedélyek", ro="Permisiuni Android", bg="Разрешения за Android",
        el="Άδειες Android", tr="Android izinleri", sv="Android-behörigheter",
        da="Android-tilladelser", nb="Android-tillatelser", fi="Android-käyttöoikeudet",
        et="Androidi load", lv="Android atļaujas", lt="Android leidimai",
        hr="Android dopuštenja", sl="Dovoljenja za Android", sr_Latn="Android dozvole",
        bs="Android dozvole", mk="Android дозволи", sq="Lejet e Android",
        is_="Android-heimildir", ca="Permisos d’Android", ga="Ceadanna Android",
        mt="Permessi Android", zh_CN="Android 权限", ja="Androidの権限",
        ko="Android 권한", vi="Quyền Android",
    ))
    s_use = t(lang, L(
        en="How we use information", ru="Как мы используем информацию", uk="Як ми використовуємо інформацію",
        by="Як мы выкарыстоўваем інфармацыю",
        de="Wie wir Informationen verwenden", fr="Comment nous utilisons les informations",
        es="Cómo usamos la información", it="Come usiamo le informazioni",
        pt="Como usamos a informação", nl="Hoe we informatie gebruiken",
        pl="Jak wykorzystujemy informacje", cs="Jak údaje používáme", sk="Ako údaje používame",
        hu="Hogyan használjuk az adatokat", ro="Cum folosim informațiile",
        bg="Как използваме информацията", el="Πώς χρησιμοποιούμε τις πληροφορίες",
        tr="Bilgileri nasıl kullanıyoruz", sv="Hur vi använder information",
        da="Sådan bruger vi oplysninger", nb="Hvordan vi bruker informasjon",
        fi="Miten käytämme tietoja", et="Kuidas teavet kasutame",
        lv="Kā mēs izmantojam informāciju", lt="Kaip naudojame informaciją",
        hr="Kako koristimo podatke", sl="Kako uporabljamo podatke",
        sr_Latn="Kako koristimo podatke", bs="Kako koristimo podatke",
        mk="Како ги користиме информациите", sq="Si i përdorim informacionet",
        is_="Hvernig við notum upplýsingar", ca="Com fem servir la informació",
        ga="Conas a úsáidimid faisnéis", mt="Kif nużaw l-informazzjoni",
        zh_CN="我们如何使用信息", ja="情報の利用方法", ko="정보 이용 방법", vi="Chúng tôi dùng thông tin như thế nào",
    ))
    s_third = t(lang, L(
        en="Third-party services", ru="Сторонние сервисы", uk="Сторонні сервіси", by="Староннія сэрвісы",
        de="Drittanbieterdienste", fr="Services tiers", es="Servicios de terceros",
        it="Servizi di terze parti", pt="Serviços de terceiros", nl="Diensten van derden",
        pl="Usługi stron trzecich", cs="Služby třetích stran", sk="Služby tretích strán",
        hu="Harmadik felek szolgáltatásai", ro="Servicii terțe", bg="Услуги на трети страни",
        el="Υπηρεσίες τρίτων", tr="Üçüncü taraf hizmetler", sv="Tredjepartstjänster",
        da="Tredjepartstjenester", nb="Tredjepartstjenester", fi="Kolmansien osapuolten palvelut",
        et="Kolmandate osapoolte teenused", lv="Trešo pušu pakalpojumi", lt="Trečiųjų šalių paslaugos",
        hr="Usluge trećih strana", sl="Storitve tretjih oseb", sr_Latn="Usluge trećih strana",
        bs="Usluge trećih strana", mk="Услуги од трети страни", sq="Shërbime të palëve të treta",
        is_="Þjónusta þriðja aðila", ca="Serveis de tercers", ga="Seirbhísí tríú páirtí",
        mt="Servizzi ta’ partijiet terzi", zh_CN="第三方服务", ja="サードパーティのサービス",
        ko="제3자 서비스", vi="Dịch vụ bên thứ ba",
    ))
    s_store = t(lang, L(
        en="Data storage and retention", ru="Хранение и сроки", uk="Зберігання та строки",
        by="Захаванне і тэрміны",
        de="Speicherung und Aufbewahrung", fr="Stockage et conservation",
        es="Almacenamiento y retención", it="Conservazione dei dati",
        pt="Armazenamento e retenção", nl="Opslag en bewaartermijn",
        pl="Przechowywanie danych", cs="Ukládání a uchovávání", sk="Ukladanie a uchovávanie",
        hu="Adattárolás és megőrzés", ro="Stocare și păstrare", bg="Съхранение на данни",
        el="Αποθήκευση και διατήρηση", tr="Veri saklama", sv="Lagring och bevarande",
        da="Opbevaring", nb="Lagring og oppbevaring", fi="Tallennus ja säilytys",
        et="Andmete säilitamine", lv="Datu glabāšana", lt="Duomenų saugojimas",
        hr="Pohrana podataka", sl="Hranjenje podatkov", sr_Latn="Čuvanje podataka",
        bs="Čuvanje podataka", mk="Чување на податоци", sq="Ruajtja e të dhënave",
        is_="Geymsla gagna", ca="Emmagatzematge i retenció", ga="Stóráil agus coinneáil",
        mt="Ħażna u żamma", zh_CN="数据存储与保留", ja="データの保存",
        ko="데이터 저장 및 보관", vi="Lưu trữ và giữ lại dữ liệu",
    ))
    s_sec = t(lang, L(
        en="Security", ru="Безопасность", uk="Безпека", by="Бяспека",
        de="Sicherheit", fr="Sécurité", es="Seguridad", it="Sicurezza",
        pt="Segurança", nl="Beveiliging", pl="Bezpieczeństwo", cs="Zabezpečení", sk="Zabezpečenie",
        hu="Biztonság", ro="Securitate", bg="Сигурност", el="Ασφάλεια", tr="Güvenlik",
        sv="Säkerhet", da="Sikkerhed", nb="Sikkerhet", fi="Turvallisuus", et="Turvalisus",
        lv="Drošība", lt="Saugumas", hr="Sigurnost", sl="Varnost", sr_Latn="Bezbednost",
        bs="Sigurnost", mk="Безбедност", sq="Siguria", is_="Öryggi", ca="Seguretat",
        ga="Slándáil", mt="Sigurtà", zh_CN="安全", ja="セキュリティ", ko="보안", vi="Bảo mật",
    ))
    s_child = t(lang, L(
        en="Children", ru="Дети", uk="Діти", by="Дзеці",
        de="Kinder", fr="Enfants", es="Niños", it="Minori",
        pt="Crianças", nl="Kinderen", pl="Dzieci", cs="Děti", sk="Deti",
        hu="Gyermekek", ro="Copii", bg="Деца", el="Παιδιά", tr="Çocuklar",
        sv="Barn", da="Børn", nb="Barn", fi="Lapset", et="Lapsed",
        lv="Bērni", lt="Vaikai", hr="Djeca", sl="Otroci", sr_Latn="Deca",
        bs="Djeca", mk="Деца", sq="Fëmijët", is_="Börn", ca="Infants",
        ga="Leanaí", mt="Tfal", zh_CN="儿童", ja="お子様", ko="아동", vi="Trẻ em",
    ))
    s_rights = t(lang, L(
        en="Your rights", ru="Ваши права", uk="Ваші права", by="Вашы правы",
        de="Ihre Rechte", fr="Vos droits", es="Sus derechos", it="I tuoi diritti",
        pt="Os seus direitos", nl="Uw rechten", pl="Twoje prawa", cs="Vaše práva", sk="Vaše práva",
        hu="Az Ön jogai", ro="Drepturile dvs.", bg="Вашите права", el="Τα δικαιώματά σας",
        tr="Haklarınız", sv="Dina rättigheter", da="Dine rettigheder", nb="Dine rettigheter",
        fi="Oikeutesi", et="Teie õigused", lv="Jūsu tiesības", lt="Jūsų teisės",
        hr="Vaša prava", sl="Vaše pravice", sr_Latn="Vaša prava", bs="Vaša prava",
        mk="Вашите права", sq="Të drejtat tuaja", is_="Réttindi þín", ca="Els vostres drets",
        ga="Do chearta", mt="Id-drittijiet tiegħek", zh_CN="您的权利", ja="お客様の権利",
        ko="귀하의 권리", vi="Quyền của bạn",
    ))
    s_chg = t(lang, L(
        en="Changes", ru="Изменения", uk="Зміни", by="Змены",
        de="Änderungen", fr="Modifications", es="Cambios", it="Modifiche",
        pt="Alterações", nl="Wijzigingen", pl="Zmiany", cs="Změny", sk="Zmeny",
        hu="Változások", ro="Modificări", bg="Промени", el="Αλλαγές", tr="Değişiklikler",
        sv="Ändringar", da="Ændringer", nb="Endringer", fi="Muutokset", et="Muudatused",
        lv="Izmaiņas", lt="Pakeitimai", hr="Izmjene", sl="Spremembe", sr_Latn="Izmene",
        bs="Izmjene", mk="Промени", sq="Ndryshimet", is_="Breytingar", ca="Canvis",
        ga="Athruithe", mt="Bidliet", zh_CN="变更", ja="変更", ko="변경", vi="Thay đổi",
    ))
    s_contact = t(lang, L(
        en="Contact", ru="Контакты", uk="Контакти", by="Кантакты",
        de="Kontakt", fr="Contact", es="Contacto", it="Contatti",
        pt="Contacto", nl="Contact", pl="Kontakt", cs="Kontakt", sk="Kontakt",
        hu="Kapcsolat", ro="Contact", bg="Контакт", el="Επικοινωνία", tr="İletişim",
        sv="Kontakt", da="Kontakt", nb="Kontakt", fi="Yhteystiedot", et="Kontakt",
        lv="Kontakti", lt="Kontaktai", hr="Kontakt", sl="Kontakt", sr_Latn="Kontakt",
        bs="Kontakt", mk="Контакт", sq="Kontakt", is_="Tengiliðir", ca="Contacte",
        ga="Teagmháil", mt="Kuntatt", zh_CN="联系方式", ja="お問い合わせ", ko="문의", vi="Liên hệ",
    ))

    # Intro paragraphs
    intro1 = t(lang, L(
        en=(
            "This Privacy Policy explains how <strong>PlatePrivacy</strong> (the mobile application "
            "“PlatePrivacy” / “PlatePrivacy Pro”, package <code>com.palityka.plateprivacy</code>) processes "
            "information when you use the app on Android."
        ),
        ru=(
            "Настоящая Политика конфиденциальности описывает, как приложение <strong>PlatePrivacy</strong> "
            "(«PlatePrivacy» / «PlatePrivacy Pro», пакет <code>com.palityka.plateprivacy</code>) обрабатывает "
            "информацию при использовании на Android."
        ),
        uk=(
            "Ця Політика конфіденційності пояснює, як застосунок <strong>PlatePrivacy</strong> "
            "(«PlatePrivacy» / «PlatePrivacy Pro», пакет <code>com.palityka.plateprivacy</code>) обробляє "
            "інформацію під час використання на Android."
        ),
        de=(
            "Diese Datenschutzerklärung erläutert, wie <strong>PlatePrivacy</strong> (die mobile App "
            "„PlatePrivacy“ / „PlatePrivacy Pro“, Paket <code>com.palityka.plateprivacy</code>) Informationen "
            "verarbeitet, wenn Sie die App unter Android nutzen."
        ),
        fr=(
            "La présente politique de confidentialité explique comment <strong>PlatePrivacy</strong> "
            "(l’application mobile « PlatePrivacy » / « PlatePrivacy Pro », package "
            "<code>com.palityka.plateprivacy</code>) traite les informations lorsque vous utilisez "
            "l’application sur Android."
        ),
        es=(
            "Esta Política de privacidad explica cómo <strong>PlatePrivacy</strong> (la aplicación "
            "móvil «PlatePrivacy» / «PlatePrivacy Pro», paquete <code>com.palityka.plateprivacy</code>) "
            "trata la información cuando usa la app en Android."
        ),
        it=(
            "La presente Informativa sulla privacy spiega come <strong>PlatePrivacy</strong> "
            "(l’app mobile “PlatePrivacy” / “PlatePrivacy Pro”, package <code>com.palityka.plateprivacy</code>) "
            "tratta le informazioni quando usi l’app su Android."
        ),
        pt=(
            "Esta Política de privacidade explica como o <strong>PlatePrivacy</strong> (a aplicação "
            "móvel “PlatePrivacy” / “PlatePrivacy Pro”, pacote <code>com.palityka.plateprivacy</code>) "
            "trata a informação quando usa a app no Android."
        ),
        nl=(
            "Dit privacybeleid legt uit hoe <strong>PlatePrivacy</strong> (de mobiele app "
            "“PlatePrivacy” / “PlatePrivacy Pro”, package <code>com.palityka.plateprivacy</code>) informatie "
            "verwerkt wanneer u de app op Android gebruikt."
        ),
        pl=(
            "Niniejsza Polityka prywatności wyjaśnia, jak <strong>PlatePrivacy</strong> (aplikacja "
            "mobilna „PlatePrivacy” / „PlatePrivacy Pro”, pakiet <code>com.palityka.plateprivacy</code>) "
            "przetwarza informacje podczas korzystania z aplikacji na Androidzie."
        ),
        zh_CN=(
            "本隐私政策说明 <strong>PlatePrivacy</strong>（移动应用 “PlatePrivacy” / “PlatePrivacy Pro”，"
            "包名 <code>com.palityka.plateprivacy</code>）在 Android 上使用时如何处理信息。"
        ),
        ja=(
            "本プライバシーポリシーは、<strong>PlatePrivacy</strong>（モバイルアプリ「PlatePrivacy」/"
            "「PlatePrivacy Pro」、パッケージ <code>com.palityka.plateprivacy</code>）が Android 上で"
            "どのように情報を処理するかを説明します。"
        ),
        ko=(
            "본 개인정보 처리방침은 <strong>PlatePrivacy</strong>(모바일 앱 “PlatePrivacy” / "
            "“PlatePrivacy Pro”, 패키지 <code>com.palityka.plateprivacy</code>)가 Android에서 "
            "정보를 어떻게 처리하는지 설명합니다."
        ),
        vi=(
            "Chính sách quyền riêng tư này giải thích cách <strong>PlatePrivacy</strong> "
            "(ứng dụng di động “PlatePrivacy” / “PlatePrivacy Pro”, gói "
            "<code>com.palityka.plateprivacy</code>) xử lý thông tin khi bạn dùng ứng dụng trên Android."
        ),
    ))
    intro2 = t(lang, L(
        en=(
            "PlatePrivacy blurs and masks license plates in photos and videos using blur, pixelation, or solid color. "
            "Processing runs <strong>on your device</strong>. The app does <strong>not</strong> require "
            "an account and does <strong>not</strong> upload your photos or videos to our servers."
        ),
        ru=(
            "PlatePrivacy скрывает лица на фото и видео с помощью эмодзи, цветных блоков, пикселизации "
            "или размытия. Обработка выполняется <strong>на вашем устройстве</strong>. Приложение "
            "<strong>не требует</strong> учётной записи и <strong>не загружает</strong> ваши фото "
            "и видео на наши серверы."
        ),
        uk=(
            "PlatePrivacy приховує обличчя на фото та відео за допомогою емодзі, кольорових блоків, "
            "пікселізації або розмиття. Обробка виконується <strong>на вашому пристрої</strong>. "
            "Застосунок <strong>не вимагає</strong> облікового запису та <strong>не завантажує</strong> "
            "ваші фото й відео на наші сервери."
        ),
        de=(
            "PlatePrivacy macht Kennzeichen auf Fotos und Videos mit Unschärfe, Verpixelung oder "
            "oder Weichzeichnung. Die Verarbeitung läuft <strong>auf Ihrem Gerät</strong>. Die App "
            "benötigt <strong>kein</strong> Konto und lädt Ihre Fotos oder Videos <strong>nicht</strong> "
            "auf unsere Server hoch."
        ),
        fr=(
            "PlatePrivacy masque les plaques d’immatriculation sur les photos et vidéos avec flou, "
            "de la pixellisation ou un flou. Le traitement s’effectue <strong>sur votre appareil</strong>. "
            "L’application <strong>ne nécessite pas</strong> de compte et <strong>n’envoie pas</strong> "
            "vos photos ou vidéos sur nos serveurs."
        ),
        es=(
            "PlatePrivacy oculta matrículas en fotos y vídeos con desenfoque, pixelado o color sólido. "
            "El procesamiento se realiza <strong>en su dispositivo</strong>. La app <strong>no</strong> "
            "requiere una cuenta y <strong>no</strong> sube sus fotos o vídeos a nuestros servidores."
        ),
        it=(
            "PlatePrivacy nasconde le targhe in foto e video con sfocatura, pixel o colore pieno. "
            "L’elaborazione avviene <strong>sul dispositivo</strong>. L’app <strong>non</strong> richiede "
            "un account e <strong>non</strong> carica foto o video sui nostri server."
        ),
        pt=(
            "O PlatePrivacy oculta matrículas em fotos e vídeos com desfoque, pixelização ou cor sólida. "
            "O processamento corre <strong>no seu dispositivo</strong>. A app <strong>não</strong> exige "
            "conta e <strong>não</strong> envia as suas fotos ou vídeos para os nossos servidores."
        ),
        nl=(
            "PlatePrivacy verbergt kentekens op foto’s en video’s met vervaging, pixelatie of "
            "vervaging. Verwerking gebeurt <strong>op uw apparaat</strong>. De app vereist "
            "<strong>geen</strong> account en uploadt uw foto’s of video’s <strong>niet</strong> naar "
            "onze servers."
        ),
        pl=(
            "PlatePrivacy ukrywa tablice rejestracyjne na zdjęciach i filmach za pomocą rozmycia, "
            "pikselizacji lub rozmycia. Przetwarzanie odbywa się <strong>na urządzeniu</strong>. "
            "Aplikacja <strong>nie</strong> wymaga konta i <strong>nie</strong> przesyła zdjęć ani "
            "filmów na nasze serwery."
        ),
        zh_CN=(
            "PlatePrivacy 使用表情、色块、像素化或模糊来遮挡照片和视频中的面孔。处理在"
            "<strong>您的设备上</strong>完成。应用<strong>不需要</strong>账号，也"
            "<strong>不会</strong>将您的照片或视频上传到我们的服务器。"
        ),
        ja=(
            "PlatePrivacy は絵文字・色ブロック・モザイク・ぼかしで写真や動画の顔を隠します。"
            "処理は<strong>端末上</strong>で行われます。アカウントは<strong>不要</strong>で、"
            "写真や動画を当社サーバーに<strong>アップロードしません</strong>。"
        ),
        ko=(
            "PlatePrivacy는 이모지, 색 블록, 픽셀화 또는 흐림으로 사진·동영상의 얼굴을 가립니다. "
            "처리는 <strong>기기에서</strong> 이루어집니다. 계정은 <strong>필요 없으며</strong> "
            "사진·동영상을 저희 서버에 <strong>업로드하지 않습니다</strong>."
        ),
        vi=(
            "PlatePrivacy làm mờ biển số trên ảnh và video bằng blur, pixel hoặc màu đặc. "
            "Xử lý chạy <strong>trên thiết bị của bạn</strong>. Ứng dụng <strong>không</strong> "
            "yêu cầu tài khoản và <strong>không</strong> tải ảnh/video lên máy chủ của chúng tôi."
        ),
    ))

    ctrl = t(lang, L(
        en=f"<strong>Controller:</strong> Pavel Palityka<br><strong>Contact:</strong> {MAIL}",
        ru=f"<strong>Оператор:</strong> Pavel Palityka<br><strong>Контакт:</strong> {MAIL}",
        uk=f"<strong>Контролер:</strong> Pavel Palityka<br><strong>Контакт:</strong> {MAIL}",
        de=f"<strong>Verantwortlicher:</strong> Pavel Palityka<br><strong>Kontakt:</strong> {MAIL}",
        fr=f"<strong>Responsable :</strong> Pavel Palityka<br><strong>Contact :</strong> {MAIL}",
        es=f"<strong>Responsable:</strong> Pavel Palityka<br><strong>Contacto:</strong> {MAIL}",
        it=f"<strong>Titolare:</strong> Pavel Palityka<br><strong>Contatto:</strong> {MAIL}",
        pt=f"<strong>Responsável:</strong> Pavel Palityka<br><strong>Contacto:</strong> {MAIL}",
        nl=f"<strong>Verantwoordelijke:</strong> Pavel Palityka<br><strong>Contact:</strong> {MAIL}",
        pl=f"<strong>Administrator:</strong> Pavel Palityka<br><strong>Kontakt:</strong> {MAIL}",
        zh_CN=f"<strong>控制者：</strong> Pavel Palityka<br><strong>联系：</strong> {MAIL}",
        ja=f"<strong>管理者：</strong> Pavel Palityka<br><strong>連絡先：</strong> {MAIL}",
        ko=f"<strong>관리자:</strong> Pavel Palityka<br><strong>연락처:</strong> {MAIL}",
        vi=f"<strong>Đơn vị kiểm soát:</strong> Pavel Palityka<br><strong>Liên hệ:</strong> {MAIL}",
    ))

    info_lead = t(lang, L(
        en="Depending on how you use PlatePrivacy, the following categories of data may be processed:",
        ru="В зависимости от того, как вы используете PlatePrivacy, могут обрабатываться следующие категории данных:",
        uk="Залежно від використання PlatePrivacy можуть оброблятися такі категорії даних:",
        de="Je nachdem, wie Sie PlatePrivacy nutzen, können folgende Datenkategorien verarbeitet werden:",
        fr="Selon votre utilisation de PlatePrivacy, les catégories de données suivantes peuvent être traitées :",
        es="Según cómo use PlatePrivacy, pueden tratarse las siguientes categorías de datos:",
        it="A seconda di come usi PlatePrivacy, possono essere elaborate le seguenti categorie di dati:",
        pt="Consoante a utilização do PlatePrivacy, podem ser processadas as seguintes categorias de dados:",
        nl="Afhankelijk van hoe u PlatePrivacy gebruikt, kunnen de volgende gegevenscategorieën worden verwerkt:",
        pl="W zależności od sposobu korzystania z PlatePrivacy mogą być przetwarzane następujące kategorie danych:",
        zh_CN="根据您使用 PlatePrivacy 的方式，可能处理以下类别的数据：",
        ja="PlatePrivacy の使い方に応じて、次の種類のデータが処理される場合があります：",
        ko="PlatePrivacy 사용 방식에 따라 다음 범주의 데이터가 처리될 수 있습니다:",
        vi="Tùy cách bạn dùng PlatePrivacy, các loại dữ liệu sau có thể được xử lý:",
    ))

    items_info = [
        t(lang, L(
            en=(
                "<strong>Photos and videos on your device</strong> — files you pick, share into the app, "
                "or capture with the camera. They are read and processed locally to detect license plates and apply "
                "masks. Output files are saved where you choose (for example your gallery or a folder you "
                "select). We do not receive copies of this media."
            ),
            ru=(
                "<strong>Фото и видео на устройстве</strong> — файлы, которые вы выбираете, отправляете "
                "в приложение или снимаете камерой. Они читаются и обрабатываются локально для обнаружения "
                "номеров и наложения масок. Результат сохраняется туда, куда вы укажете. Мы не получаем копии "
                "этих материалов."
            ),
            uk=(
                "<strong>Фото та відео на пристрої</strong> — файли, які ви обираєте, надсилаєте в "
                "застосунок або знімаєте камерою. Вони читаються та обробляються локально. Ми не отримуємо "
                "копій цих матеріалів."
            ),
            de=(
                "<strong>Fotos und Videos auf Ihrem Gerät</strong> — Dateien, die Sie auswählen, teilen "
                "oder mit der Kamera aufnehmen. Sie werden lokal gelesen und verarbeitet. Wir erhalten "
                "keine Kopien dieser Medien."
            ),
            fr=(
                "<strong>Photos et vidéos sur votre appareil</strong> — fichiers que vous choisissez, "
                "partagez ou capturez. Ils sont lus et traités localement. Nous ne recevons pas de copies."
            ),
            es=(
                "<strong>Fotos y vídeos en su dispositivo</strong> — archivos que elige, comparte o "
                "captura. Se leen y procesan localmente. No recibimos copias de estos medios."
            ),
            it=(
                "<strong>Foto e video sul dispositivo</strong> — file che selezioni, condividi o "
                "acquisisci. Sono letti ed elaborati in locale. Non riceviamo copie di questi media."
            ),
            pt=(
                "<strong>Fotos e vídeos no dispositivo</strong> — ficheiros que escolhe, partilha ou "
                "captura. São lidos e processados localmente. Não recebemos cópias destes conteúdos."
            ),
            nl=(
                "<strong>Foto’s en video’s op uw apparaat</strong> — bestanden die u kiest, deelt of "
                "opneemt. Ze worden lokaal gelezen en verwerkt. Wij ontvangen geen kopieën."
            ),
            pl=(
                "<strong>Zdjęcia i filmy na urządzeniu</strong> — pliki, które wybierasz, udostępniasz "
                "lub nagrywasz. Są odczytywane i przetwarzane lokalnie. Nie otrzymujemy ich kopii."
            ),
            zh_CN=(
                "<strong>设备上的照片和视频</strong> — 您选择、分享或拍摄的文件。在本地读取和处理。"
                "我们不会收到这些媒体的副本。"
            ),
            ja=(
                "<strong>端末上の写真・動画</strong> — 選択・共有・撮影したファイル。端末内で読み取り・"
                "処理します。当社がコピーを受け取ることはありません。"
            ),
            ko=(
                "<strong>기기의 사진·동영상</strong> — 선택·공유·촬영한 파일. 기기에서 읽고 처리합니다. "
                "저희는 사본을 받지 않습니다."
            ),
            vi=(
                "<strong>Ảnh và video trên thiết bị</strong> — tệp bạn chọn, chia sẻ hoặc quay. "
                "Được đọc và xử lý cục bộ. Chúng tôi không nhận bản sao."
            ),
        )),
        t(lang, L(
            en=(
                "<strong>License plate detection data</strong> — bounding boxes and related metadata used only "
                "during editing and video processing on the device. Plate detection uses a local ONNX "
                "model (LPD-YuNet). This data is not sent to us."
            ),
            ru=(
                "<strong>Данные детекции номеров</strong> — координаты рамок и связанные метаданные только "
                "при редактировании на устройстве. Детекция — локальная ONNX-модель (LPD-YuNet). Нам не "
                "передаётся."
            ),
            uk=(
                "<strong>Дані виявлення облич</strong> — координати рамок і метадані лише під час "
                "редагування на пристрої. Локальна ONNX-модель (LPD-YuNet). Нам не передаються."
            ),
            de=(
                "<strong>Gesichtserkennungsdaten</strong> — Bounding Boxes und Metadaten nur während "
                "der Bearbeitung auf dem Gerät. Lokales ONNX-Modell (LPD-YuNet). Werden nicht an uns gesendet."
            ),
            fr=(
                "<strong>Données de détection de visages</strong> — boîtes et métadonnées utilisées "
                "uniquement sur l’appareil. Modèle ONNX local (LPD-YuNet). Non envoyées chez nous."
            ),
            es=(
                "<strong>Datos de detección facial</strong> — recuadros y metadatos solo en el "
                "dispositivo. Modelo ONNX local (LPD-YuNet). No se nos envían."
            ),
            it=(
                "<strong>Dati di rilevamento volti</strong> — riquadri e metadati solo sul dispositivo. "
                "Modello ONNX locale (LPD-YuNet). Non vengono inviati a noi."
            ),
            pt=(
                "<strong>Dados de deteção facial</strong> — caixas e metadados só no dispositivo. "
                "Modelo ONNX local (LPD-YuNet). Não nos são enviados."
            ),
            nl=(
                "<strong>Gezichtsdetectiegegevens</strong> — kaders en metadata alleen op het apparaat. "
                "Lokaal ONNX-model (LPD-YuNet). Worden niet naar ons gestuurd."
            ),
            pl=(
                "<strong>Dane wykrywania twarzy</strong> — ramki i metadane tylko na urządzeniu. "
                "Lokalny model ONNX (LPD-YuNet). Nie są do nas wysyłane."
            ),
            zh_CN=(
                "<strong>人脸检测数据</strong> — 仅在设备上编辑时使用的框与元数据。本地 ONNX 模型"
                "（LPD-YuNet）。不会发送给我们。"
            ),
            ja=(
                "<strong>顔検出データ</strong> — 端末上の編集時のみ使う枠とメタデータ。ローカル "
                "ONNX モデル（LPD-YuNet）。当社には送信されません。"
            ),
            ko=(
                "<strong>얼굴 감지 데이터</strong> — 기기에서 편집할 때만 쓰는 박스·메타데이터. "
                "로컬 ONNX 모델(LPD-YuNet). 저희에게 전송되지 않습니다."
            ),
            vi=(
                "<strong>Dữ liệu phát hiện khuôn mặt</strong> — hộp và metadata chỉ trên thiết bị. "
                "Mô hình ONNX cục bộ (LPD-YuNet). Không gửi cho chúng tôi."
            ),
        )),
        t(lang, L(
            en=(
                "<strong>App settings and recent list</strong> — theme, language, cover "
                "style, and a local list of recent jobs stored on your device."
            ),
            ru=(
                "<strong>Настройки и список недавних</strong> — тема, язык, стиль маски и "
                "локальный список недавних работ на устройстве."
            ),
            uk=(
                "<strong>Налаштування та список недавніх</strong> — тема, мова, емодзі, стиль маски та "
                "локальний список недавніх робіт на пристрої."
            ),
            de=(
                "<strong>App-Einstellungen und Zuletzt-Liste</strong> — Thema, Sprache, Maskenstil "
                "und lokale Liste der letzten Arbeiten auf dem Gerät."
            ),
            fr=(
                "<strong>Paramètres et liste des récents</strong> — thème, langue, style de masque "
                "et liste locale des travaux récents sur l’appareil."
            ),
            es=(
                "<strong>Ajustes y lista de recientes</strong> — tema, idioma, estilo de máscara "
                "y lista local de trabajos recientes en el dispositivo."
            ),
            it=(
                "<strong>Impostazioni e elenco recenti</strong> — tema, lingua, stile maschera e "
                "elenco locale dei lavori recenti sul dispositivo."
            ),
            pt=(
                "<strong>Definições e lista de recentes</strong> — tema, idioma, estilo de máscara "
                "e lista local de trabalhos recentes no dispositivo."
            ),
            nl=(
                "<strong>Instellingen en recente lijst</strong> — thema, taal, maskerstijl en "
                "lokale lijst van recente taken op het apparaat."
            ),
            pl=(
                "<strong>Ustawienia i lista ostatnich</strong> — motyw, język, styl maski oraz "
                "lokalna lista ostatnich prac na urządzeniu."
            ),
            zh_CN="<strong>应用设置与最近列表</strong> — 主题、语言、表情、遮罩样式及设备上的最近任务列表。",
            ja="<strong>設定と最近の一覧</strong> — テーマ、言語、絵文字、マスクスタイル、端末上の最近の作業一覧。",
            ko="<strong>앱 설정 및 최근 목록</strong> — 테마, 언어, 이모지, 마스크 스타일, 기기의 최근 작업 목록.",
            vi="<strong>Cài đặt và danh sách gần đây</strong> — chủ đề, ngôn ngữ, kiểu mặt nạ và danh sách công việc gần đây trên thiết bị.",
        )),
        t(lang, L(
            en=(
                "<strong>Camera capture</strong> — if you take a photo or video with the in-app camera, "
                "the file is stored in the app’s cache on your device for editing."
            ),
            ru=(
                "<strong>Съёмка камерой</strong> — фото или видео через камеру приложения сохраняется "
                "в кэше приложения на устройстве для редактирования."
            ),
            uk=(
                "<strong>Зйомка камерою</strong> — фото або відео через камеру застосунку зберігається "
                "в кеші на пристрої для редагування."
            ),
            de=(
                "<strong>Kameraaufnahme</strong> — Foto oder Video über die App-Kamera wird im Cache "
                "auf dem Gerät für die Bearbeitung gespeichert."
            ),
            fr=(
                "<strong>Capture caméra</strong> — photo ou vidéo via la caméra de l’app stockée dans "
                "le cache de l’appareil pour l’édition."
            ),
            es=(
                "<strong>Captura con cámara</strong> — foto o vídeo con la cámara de la app se guarda "
                "en la caché del dispositivo para editar."
            ),
            it=(
                "<strong>Scatto con fotocamera</strong> — foto o video con la fotocamera in-app salvati "
                "nella cache del dispositivo per la modifica."
            ),
            pt=(
                "<strong>Captura com câmara</strong> — foto ou vídeo pela câmara da app é guardado na "
                "cache do dispositivo para edição."
            ),
            nl=(
                "<strong>Camera-opname</strong> — foto of video via de in-app-camera wordt in de cache "
                "op het apparaat bewaard om te bewerken."
            ),
            pl=(
                "<strong>Nagranie kamerą</strong> — zdjęcie lub film z kamery w aplikacji trafia do "
                "pamięci podręcznej na urządzeniu do edycji."
            ),
            zh_CN="<strong>相机拍摄</strong> — 应用内拍摄的照片或视频保存在设备缓存中以便编辑。",
            ja="<strong>カメラ撮影</strong> — アプリ内カメラで撮った写真・動画は編集用に端末キャッシュに保存されます。",
            ko="<strong>카메라 촬영</strong> — 앱 내 카메라로 찍은 사진·동영상은 편집을 위해 기기 캐시에 저장됩니다.",
            vi="<strong>Chụp/quay bằng camera</strong> — ảnh hoặc video từ camera trong app được lưu trong bộ nhớ đệm thiết bị để chỉnh sửa.",
        )),
        t(lang, L(
            en=(
                "<strong>Purchase status</strong> — whether you unlocked PlatePrivacy Pro via Google Play "
                "in-app billing. Verification is handled by Google; we store only the Pro/unlock flag "
                "on your device."
            ),
            ru=(
                "<strong>Статус покупки</strong> — разблокирован ли PlatePrivacy Pro через Google Play. "
                "Проверку выполняет Google; на устройстве хранится только флаг Pro."
            ),
            uk=(
                "<strong>Статус покупки</strong> — чи розблоковано PlatePrivacy Pro через Google Play; "
                "на пристрої зберігається лише прапорець Pro."
            ),
            de=(
                "<strong>Kaufstatus</strong> — ob PlatePrivacy Pro über Google Play freigeschaltet wurde. "
                "Die Prüfung erfolgt durch Google; auf dem Gerät speichern wir nur das Pro-Flag."
            ),
            fr=(
                "<strong>Statut d’achat</strong> — si PlatePrivacy Pro est débloqué via Google Play. "
                "La vérification est faite par Google ; nous stockons uniquement le drapeau Pro."
            ),
            es=(
                "<strong>Estado de compra</strong> — si desbloqueó PlatePrivacy Pro con Google Play. "
                "Google verifica; en el dispositivo solo guardamos el indicador Pro."
            ),
            it=(
                "<strong>Stato acquisto</strong> — se hai sbloccato PlatePrivacy Pro via Google Play. "
                "La verifica è di Google; sul dispositivo resta solo il flag Pro."
            ),
            pt=(
                "<strong>Estado de compra</strong> — se desbloqueou o PlatePrivacy Pro via Google Play. "
                "A verificação é da Google; no dispositivo guardamos só o sinal Pro."
            ),
            nl=(
                "<strong>Aankoopstatus</strong> — of PlatePrivacy Pro via Google Play is ontgrendeld. "
                "Google verifieert; op het apparaat bewaren we alleen de Pro-vlag."
            ),
            pl=(
                "<strong>Status zakupu</strong> — czy odblokowano PlatePrivacy Pro przez Google Play. "
                "Weryfikację prowadzi Google; na urządzeniu tylko flaga Pro."
            ),
            zh_CN=(
                "<strong>购买状态</strong> — 是否通过 Google Play 解锁 PlatePrivacy Pro。由 Google 验证；"
                "设备上仅保存 Pro 标志。"
            ),
            ja=(
                "<strong>購入状態</strong> — Google Play 経由で PlatePrivacy Pro を解除したか。"
                "検証は Google、端末には Pro フラグのみ保存。"
            ),
            ko=(
                "<strong>구매 상태</strong> — Google Play로 PlatePrivacy Pro 잠금 해제 여부. "
                "검증은 Google이 하며, 기기에는 Pro 플래그만 저장됩니다."
            ),
            vi=(
                "<strong>Trạng thái mua</strong> — đã mở PlatePrivacy Pro qua Google Play hay chưa. "
                "Google xác minh; trên thiết bị chỉ lưu cờ Pro."
            ),
        )),
        t(lang, L(
            en=(
                "<strong>Advertising data (free version)</strong> — if you use the free edition with ads, "
                "Appodeal and its mediated ad networks may collect your advertising identifier (GAID), "
                "IP address, device and network information, and ad interaction data (see Third parties)."
            ),
            ru=(
                "<strong>Рекламные данные (бесплатная версия)</strong> — Appodeal и связанные сети могут "
                "собирать GAID, IP-адрес, сведения об устройстве и сети, а также данные о взаимодействии "
                "с рекламой (см. «Сторонние сервисы»)."
            ),
            uk=(
                "<strong>Рекламні дані (безкоштовна версія)</strong> — Appodeal і пов’язані мережі можуть "
                "збирати GAID, IP-адресу та дані про взаємодію з рекламою."
            ),
            de=(
                "<strong>Werbedaten (Gratisversion)</strong> — Appodeal und Partner können GAID, "
                "IP-Adresse sowie Geräte- und Interaktionsdaten erheben (siehe Drittanbieter)."
            ),
            fr=(
                "<strong>Données publicitaires (version gratuite)</strong> — Appodeal et ses partenaires "
                "peuvent collecter le GAID, l’adresse IP et des données d’interaction (voir Tiers)."
            ),
            es=(
                "<strong>Datos publicitarios (versión gratuita)</strong> — Appodeal y redes asociadas "
                "pueden recopilar GAID, IP y datos de interacción (ver Terceros)."
            ),
            it=(
                "<strong>Dati pubblicitari (versione gratuita)</strong> — Appodeal e le reti mediate "
                "possono raccogliere GAID, IP e dati di interazione (vedi Terze parti)."
            ),
            pt=(
                "<strong>Dados publicitários (versão gratuita)</strong> — Appodeal e redes mediadas "
                "podem recolher GAID, IP e dados de interação (ver Terceiros)."
            ),
            nl=(
                "<strong>Advertentiegegevens (gratis versie)</strong> — Appodeal en partners kunnen "
                "GAID, IP-adres en interactiegegevens verzamelen (zie Derden)."
            ),
            pl=(
                "<strong>Dane reklamowe (wersja darmowa)</strong> — Appodeal i sieci partnerskie mogą "
                "zbierać GAID, adres IP i dane interakcji (zob. Strony trzecie)."
            ),
            zh_CN=(
                "<strong>广告数据（免费版）</strong> — Appodeal 及其广告网络可能收集广告标识符（GAID）、"
                "IP 地址、设备与网络信息及广告互动数据（见第三方）。"
            ),
            ja=(
                "<strong>広告データ（無料版）</strong> — Appodeal および配信ネットワークが GAID、"
                "IP、端末・ネットワーク情報、広告操作データを収集する場合があります（第三者参照）。"
            ),
            ko=(
                "<strong>광고 데이터(무료 버전)</strong> — Appodeal 및 광고 네트워크가 GAID, IP, "
                "기기·네트워크 정보, 광고 상호작용 데이터를 수집할 수 있습니다(제3자 참조)."
            ),
            vi=(
                "<strong>Dữ liệu quảng cáo (bản miễn phí)</strong> — Appodeal và mạng quảng cáo có thể "
                "thu thập GAID, IP và dữ liệu tương tác quảng cáo (xem Bên thứ ba)."
            ),
        )),
    ]

    info_tail = t(lang, L(
        en=(
            "We do <strong>not</strong> knowingly collect your name, email address, or phone number "
            "through the app itself unless you contact us by email."
        ),
        ru=(
            "Мы <strong>не</strong> собираем ваше имя, e-mail или телефон через само приложение, "
            "если только вы сами не напишете нам на почту."
        ),
        uk=(
            "Ми <strong>не</strong> збираємо ваше ім’я, e-mail чи телефон через сам застосунок, "
            "якщо ви самі не напишете нам."
        ),
        de=(
            "Wir erheben über die App selbst <strong>nicht</strong> wissentlich Ihren Namen, Ihre "
            "E-Mail-Adresse oder Telefonnummer, es sei denn, Sie schreiben uns per E-Mail."
        ),
        fr=(
            "Nous ne collectons <strong>pas</strong> sciemment votre nom, e-mail ou téléphone via "
            "l’application elle-même, sauf si vous nous écrivez."
        ),
        es=(
            "<strong>No</strong> recopilamos conscientemente su nombre, correo o teléfono a través "
            "de la app, salvo que nos escriba por correo."
        ),
        it=(
            "<strong>Non</strong> raccogliamo consapevolmente nome, e-mail o telefono tramite l’app, "
            "salvo che tu ci scriva via e-mail."
        ),
        pt=(
            "<strong>Não</strong> recolhemos de forma consciente o seu nome, e-mail ou telefone pela "
            "app, salvo se nos contactar por e-mail."
        ),
        nl=(
            "Wij verzamelen via de app zelf <strong>niet</strong> bewust uw naam, e-mail of telefoon, "
            "tenzij u ons mailt."
        ),
        pl=(
            "<strong>Nie</strong> zbieramy świadomie imienia, e-maila ani telefonu przez samą "
            "aplikację, chyba że napiszesz do nas e-mailem."
        ),
        zh_CN="除非您主动发邮件联系我们，我们<strong>不会</strong>通过应用本身故意收集您的姓名、邮箱或电话。",
        ja="メールでご連絡いただいた場合を除き、アプリ自体を通じて氏名・メール・電話を意図的に収集することは<strong>ありません</strong>。",
        ko="이메일로 문의하지 않는 한, 앱 자체로 이름·이메일·전화번호를 고의로 수집하지 <strong>않습니다</strong>.",
        vi=(
            "Chúng tôi <strong>không</strong> cố ý thu thập tên, email hay số điện thoại qua chính "
            "ứng dụng, trừ khi bạn gửi email cho chúng tôi."
        ),
    ))

    perm_lead = t(lang, L(
        en="The app may request permissions required for its features:",
        ru="Приложение может запрашивать разрешения, необходимые для работы функций:",
        uk="Застосунок може запитувати дозволи, необхідні для роботи функцій:",
        de="Die App kann Berechtigungen anfordern, die für Funktionen nötig sind:",
        fr="L’application peut demander les autorisations nécessaires à ses fonctions :",
        es="La app puede solicitar los permisos necesarios para sus funciones:",
        it="L’app può richiedere le autorizzazioni necessarie alle sue funzioni:",
        pt="A app pode pedir as permissões necessárias às suas funções:",
        nl="De app kan machtigingen vragen die nodig zijn voor de functies:",
        pl="Aplikacja może prosić o uprawnienia potrzebne do działania funkcji:",
        zh_CN="应用可能请求其功能所需的权限：",
        ja="アプリは機能に必要な権限を求めることがあります：",
        ko="앱은 기능에 필요한 권한을 요청할 수 있습니다:",
        vi="Ứng dụng có thể yêu cầu các quyền cần cho tính năng:",
    ))

    items_perm = [
        t(lang, L(
            en="<strong>Read images / video</strong> — to open photos and videos you select (MediaStore and the system document picker).",
            ru="<strong>Чтение изображений / видео</strong> — открытие выбранных фото и видео (MediaStore и системный выбор файлов).",
            uk="<strong>Читання зображень / відео</strong> — відкриття обраних фото та відео.",
            de="<strong>Bilder / Videos lesen</strong> — Öffnen ausgewählter Fotos und Videos.",
            fr="<strong>Lire images / vidéos</strong> — ouvrir les photos et vidéos sélectionnées.",
            es="<strong>Leer imágenes / vídeo</strong> — abrir fotos y vídeos seleccionados.",
            it="<strong>Lettura immagini / video</strong> — aprire foto e video selezionati.",
            pt="<strong>Ler imagens / vídeo</strong> — abrir fotos e vídeos selecionados.",
            nl="<strong>Afbeeldingen / video lezen</strong> — geselecteerde foto’s en video’s openen.",
            pl="<strong>Odczyt obrazów / wideo</strong> — otwieranie wybranych zdjęć i filmów.",
            zh_CN="<strong>读取图片/视频</strong> — 打开您选择的照片和视频。",
            ja="<strong>画像/動画の読み取り</strong> — 選択した写真・動画を開くため。",
            ko="<strong>이미지/동영상 읽기</strong> — 선택한 사진·동영상 열기.",
            vi="<strong>Đọc ảnh / video</strong> — mở ảnh và video bạn chọn.",
        )),
        t(lang, L(
            en="<strong>Camera</strong> — optional capture of a new photo or video for editing.",
            ru="<strong>Камера</strong> — необязательная съёмка нового фото или видео для редактирования.",
            uk="<strong>Камера</strong> — необов’язкова зйомка фото або відео для редагування.",
            de="<strong>Kamera</strong> — optionale Aufnahme eines Fotos oder Videos zur Bearbeitung.",
            fr="<strong>Caméra</strong> — capture facultative d’une photo ou vidéo pour l’édition.",
            es="<strong>Cámara</strong> — captura opcional de foto o vídeo para editar.",
            it="<strong>Fotocamera</strong> — acquisizione opzionale di foto o video da modificare.",
            pt="<strong>Câmara</strong> — captura opcional de foto ou vídeo para editar.",
            nl="<strong>Camera</strong> — optioneel een foto of video maken om te bewerken.",
            pl="<strong>Aparat</strong> — opcjonalne nagranie zdjęcia lub filmu do edycji.",
            zh_CN="<strong>相机</strong> — 可选拍摄新照片或视频以便编辑。",
            ja="<strong>カメラ</strong> — 編集用に写真・動画を任意で撮影。",
            ko="<strong>카메라</strong> — 편집용 사진·동영상 선택적 촬영.",
            vi="<strong>Camera</strong> — tùy chọn chụp/quay để chỉnh sửa.",
        )),
        t(lang, L(
            en="<strong>Internet & network state</strong> — to load advertisements (free version) and to communicate with Google Play for purchases.",
            ru="<strong>Интернет и состояние сети</strong> — показ рекламы (бесплатная версия) и связь с Google Play для покупок.",
            uk="<strong>Інтернет і стан мережі</strong> — реклама та зв’язок із Google Play.",
            de="<strong>Internet & Netzwerkstatus</strong> — Werbung (Gratisversion) und Google Play für Käufe.",
            fr="<strong>Internet et état du réseau</strong> — publicités (version gratuite) et Google Play.",
            es="<strong>Internet y estado de red</strong> — anuncios (versión gratuita) y Google Play.",
            it="<strong>Internet e stato rete</strong> — annunci (versione gratuita) e Google Play.",
            pt="<strong>Internet e estado da rede</strong> — anúncios (versão gratuita) e Google Play.",
            nl="<strong>Internet & netwerkstatus</strong> — advertenties (gratis) en Google Play.",
            pl="<strong>Internet i stan sieci</strong> — reklamy (wersja darmowa) i Google Play.",
            zh_CN="<strong>互联网与网络状态</strong> — 加载广告（免费版）并与 Google Play 通信以完成购买。",
            ja="<strong>インターネットとネットワーク状態</strong> — 広告（無料版）と Google Play 購入。",
            ko="<strong>인터넷 및 네트워크 상태</strong> — 광고(무료) 및 Google Play 구매.",
            vi="<strong>Internet & trạng thái mạng</strong> — quảng cáo (bản miễn phí) và Google Play.",
        )),
        t(lang, L(
            en="<strong>Notifications & foreground service</strong> — to show progress while a long job runs in the background, and to notify you when processing finishes.",
            ru="<strong>Уведомления и foreground service</strong> — прогресс длительной обработки в фоне и уведомление о завершении.",
            uk="<strong>Сповіщення та foreground service</strong> — прогрес довгої обробки у фоні та сповіщення про завершення.",
            de="<strong>Benachrichtigungen & Foreground-Dienst</strong> — Fortschritt langer Jobs im Hintergrund und Abschlussmeldung.",
            fr="<strong>Notifications et service au premier plan</strong> — progression des traitements longs et fin de traitement.",
            es="<strong>Notificaciones y servicio en primer plano</strong> — progreso de trabajos largos y aviso al terminar.",
            it="<strong>Notifiche e servizio in primo piano</strong> — progresso dei lavori lunghi e avviso a fine elaborazione.",
            pt="<strong>Notificações e serviço em primeiro plano</strong> — progresso de tarefas longas e aviso ao concluir.",
            nl="<strong>Meldingen & foreground-service</strong> — voortgang van lange taken en melding bij afronden.",
            pl="<strong>Powiadomienia i usługa na pierwszym planie</strong> — postęp długich zadań i powiadomienie o końcu.",
            zh_CN="<strong>通知与前台服务</strong> — 后台长时间任务的进度，以及处理完成时的通知。",
            ja="<strong>通知とフォアグラウンドサービス</strong> — 長時間処理の進捗表示と完了通知。",
            ko="<strong>알림 및 포그라운드 서비스</strong> — 긴 작업 진행 표시와 완료 알림.",
            vi="<strong>Thông báo & dịch vụ foreground</strong> — tiến độ khi xử lý lâu ở nền và báo khi xong.",
        )),
        t(lang, L(
            en="<strong>Advertising ID</strong> — used by ad partners in the free version (see Third parties).",
            ru="<strong>Рекламный идентификатор</strong> — используется рекламными партнёрами в бесплатной версии.",
            uk="<strong>Рекламний ідентифікатор</strong> — для партнерів реклами у безкоштовній версії.",
            de="<strong>Werbe-ID</strong> — genutzt von Werbepartnern in der Gratisversion.",
            fr="<strong>Identifiant publicitaire</strong> — utilisé par les partenaires pub (version gratuite).",
            es="<strong>ID de publicidad</strong> — usado por socios publicitarios (versión gratuita).",
            it="<strong>ID pubblicitario</strong> — usato dai partner ads (versione gratuita).",
            pt="<strong>ID de publicidade</strong> — usado por parceiros de anúncios (versão gratuita).",
            nl="<strong>Advertentie-ID</strong> — gebruikt door ad-partners (gratis versie).",
            pl="<strong>Identyfikator reklamowy</strong> — używany przez partnerów reklam (wersja darmowa).",
            zh_CN="<strong>广告 ID</strong> — 免费版中广告合作方使用（见第三方）。",
            ja="<strong>広告 ID</strong> — 無料版の広告パートナーが使用（第三者参照）。",
            ko="<strong>광고 ID</strong> — 무료 버전 광고 파트너가 사용(제3자 참조).",
            vi="<strong>ID quảng cáo</strong> — dùng bởi đối tác quảng cáo bản miễn phí.",
        )),
    ]

    perm_tail = t(lang, L(
        en="You can revoke permissions in Android system settings; some features may stop working if you do.",
        ru="Разрешения можно отозвать в настройках Android; часть функций может перестать работать.",
        uk="Дозволи можна відкликати в налаштуваннях Android; частина функцій може перестати працювати.",
        de="Berechtigungen können Sie in den Android-Einstellungen widerrufen; manche Funktionen funktionieren dann ggf. nicht mehr.",
        fr="Vous pouvez retirer les autorisations dans les réglages Android ; certaines fonctions peuvent cesser de marcher.",
        es="Puede revocar permisos en los ajustes de Android; algunas funciones pueden dejar de funcionar.",
        it="Puoi revocare le autorizzazioni nelle impostazioni Android; alcune funzioni potrebbero smettere di funzionare.",
        pt="Pode revogar permissões nas definições do Android; algumas funções podem deixar de funcionar.",
        nl="U kunt machtigingen intrekken in de Android-instellingen; sommige functies werken dan mogelijk niet meer.",
        pl="Uprawnienia możesz cofnąć w ustawieniach Androida; część funkcji może przestać działać.",
        zh_CN="可在 Android 系统设置中撤销权限；撤销后部分功能可能无法使用。",
        ja="Android の設定で権限を取り消せます。取り消すと一部機能が使えなくなることがあります。",
        ko="Android 설정에서 권한을 철회할 수 있습니다. 철회 시 일부 기능이 동작하지 않을 수 있습니다.",
        vi="Bạn có thể thu hồi quyền trong cài đặt Android; một số tính năng có thể ngừng hoạt động.",
    ))

    items_use = [
        t(lang, L(
            en="Detect license plates and apply masks to photos and videos on your device",
            ru="Обнаружение номеров и наложение масок на фото и видео на устройстве",
            uk="Виявлення облич і накладання масок на фото та відео на пристрої",
            de="Gesichter erkennen und Masken auf Fotos und Videos auf dem Gerät anwenden",
            fr="Détecter les visages et appliquer des masques sur l’appareil",
            es="Detectar caras y aplicar máscaras en el dispositivo",
            it="Rilevare volti e applicare maschere sul dispositivo",
            pt="Detetar rostos e aplicar máscaras no dispositivo",
            nl="Gezichten detecteren en maskers op het apparaat toepassen",
            pl="Wykrywanie twarzy i nakładanie masek na urządzeniu",
            zh_CN="在设备上检测面孔并为照片/视频应用遮罩",
            ja="端末上で顔を検出しマスクを適用する",
            ko="기기에서 얼굴을 감지하고 마스크 적용",
            vi="Phát hiện khuôn mặt và gắn mặt nạ trên thiết bị",
        )),
        t(lang, L(
            en="Remember your settings, recent files, and editor preferences",
            ru="Сохранение настроек, недавних файлов и параметров редактора",
            uk="Збереження налаштувань, недавніх файлів і параметрів редактора",
            de="Einstellungen, letzte Dateien und Editor-Präferenzen speichern",
            fr="Mémoriser les réglages, fichiers récents et préférences de l’éditeur",
            es="Recordar ajustes, archivos recientes y preferencias del editor",
            it="Ricordare impostazioni, file recenti e preferenze dell’editor",
            pt="Memorizar definições, ficheiros recentes e preferências do editor",
            nl="Instellingen, recente bestanden en editorvoorkeuren onthouden",
            pl="Zapamiętywanie ustawień, ostatnich plików i preferencji edytora",
            zh_CN="记住设置、最近文件和编辑器偏好",
            ja="設定・最近のファイル・エディタ設定を記憶する",
            ko="설정, 최근 파일, 편집기 환경설정 저장",
            vi="Ghi nhớ cài đặt, tệp gần đây và tùy chọn trình chỉnh sửa",
        )),
        t(lang, L(
            en="Show optional ads in the free version",
            ru="Показ рекламы в бесплатной версии",
            uk="Показ реклами у безкоштовній версії",
            de="Optionale Werbung in der Gratisversion anzeigen",
            fr="Afficher des publicités optionnelles dans la version gratuite",
            es="Mostrar anuncios opcionales en la versión gratuita",
            it="Mostrare annunci opzionali nella versione gratuita",
            pt="Mostrar anúncios opcionais na versão gratuita",
            nl="Optionele advertenties tonen in de gratis versie",
            pl="Wyświetlanie opcjonalnych reklam w wersji darmowej",
            zh_CN="在免费版中显示可选广告",
            ja="無料版で任意の広告を表示する",
            ko="무료 버전에서 선택적 광고 표시",
            vi="Hiển thị quảng cáo tùy chọn ở bản miễn phí",
        )),
        t(lang, L(
            en="Process in-app purchases through Google Play",
            ru="Обработка покупок через Google Play",
            uk="Обробка покупок через Google Play",
            de="In-App-Käufe über Google Play abwickeln",
            fr="Traiter les achats in-app via Google Play",
            es="Procesar compras in-app con Google Play",
            it="Elaborare gli acquisti in-app tramite Google Play",
            pt="Processar compras na app via Google Play",
            nl="In-app-aankopen via Google Play verwerken",
            pl="Przetwarzanie zakupów w aplikacji przez Google Play",
            zh_CN="通过 Google Play 处理应用内购买",
            ja="Google Play 経由でアプリ内課金を処理する",
            ko="Google Play를 통한 인앱 결제 처리",
            vi="Xử lý mua trong ứng dụng qua Google Play",
        )),
        t(lang, L(
            en="Respond to support requests you send us",
            ru="Ответы на обращения в поддержку",
            uk="Відповіді на звернення в підтримку",
            de="Auf Support-Anfragen antworten, die Sie uns senden",
            fr="Répondre aux demandes d’assistance que vous nous envoyez",
            es="Responder a las solicitudes de soporte que nos envíe",
            it="Rispondere alle richieste di supporto che ci invii",
            pt="Responder a pedidos de suporte que nos enviar",
            nl="Reageren op supportverzoeken die u stuurt",
            pl="Odpowiadanie na zgłoszenia wsparcia, które do nas wyślesz",
            zh_CN="回复您发送的支持请求",
            ja="お送りいただいたサポート依頼に対応する",
            ko="보내주신 지원 요청에 응답",
            vi="Phản hồi yêu cầu hỗ trợ bạn gửi cho chúng tôi",
        )),
    ]

    third_lead = t(lang, L(
        en="PlatePrivacy integrates services operated by third parties:",
        ru="PlatePrivacy использует сервисы третьих лиц:",
        uk="PlatePrivacy інтегрує сервіси третіх осіб:",
        de="PlatePrivacy integriert Dienste von Drittanbietern:",
        fr="PlatePrivacy intègre des services opérés par des tiers :",
        es="PlatePrivacy integra servicios de terceros:",
        it="PlatePrivacy integra servizi gestiti da terze parti:",
        pt="O PlatePrivacy integra serviços de terceiros:",
        nl="PlatePrivacy integreert diensten van derden:",
        pl="PlatePrivacy integruje usługi stron trzecich:",
        zh_CN="PlatePrivacy 集成了第三方运营的服务：",
        ja="PlatePrivacy は第三者が運営するサービスを統合しています：",
        ko="PlatePrivacy는 제3자가 운영하는 서비스를 통합합니다:",
        vi="PlatePrivacy tích hợp dịch vụ do bên thứ ba vận hành:",
    ))

    appodeal_link = APPODEAL_RU if lang == "ru" else (APPODEAL_UK if lang == "uk" else APPODEAL)

    items_third = [
        t(lang, L(
            en=(
                f"<strong>Appodeal</strong> (free version) — advertising mediation. Appodeal and demand "
                f"partners may process IP address, advertising identifier, and ad interaction data. "
                f"See {appodeal_link}. You can limit ad personalization in your Google/Android ad settings."
            ),
            ru=(
                f"<strong>Appodeal</strong> (бесплатная версия) — медиация рекламы. Appodeal и партнёры "
                f"могут обрабатывать IP-адрес, рекламный идентификатор и данные о взаимодействии с рекламой. "
                f"См. {appodeal_link}. Ограничить персонализацию можно в настройках рекламы Google/Android."
            ),
            uk=(
                f"<strong>Appodeal</strong> (безкоштовна версія) — медіація реклами. Див. {appodeal_link}."
            ),
            de=(
                f"<strong>Appodeal</strong> (Gratisversion) — Werbemediation. Appodeal und Partner können "
                f"IP-Adresse, Werbe-ID und Interaktionsdaten verarbeiten. Siehe {appodeal_link}."
            ),
            fr=(
                f"<strong>Appodeal</strong> (version gratuite) — médiation publicitaire. Voir {appodeal_link}."
            ),
            es=(
                f"<strong>Appodeal</strong> (versión gratuita) — mediación publicitaria. Consulte {appodeal_link}."
            ),
            it=(
                f"<strong>Appodeal</strong> (versione gratuita) — mediazione pubblicitaria. Vedi {appodeal_link}."
            ),
            pt=(
                f"<strong>Appodeal</strong> (versão gratuita) — mediação publicitária. Ver {appodeal_link}."
            ),
            nl=(
                f"<strong>Appodeal</strong> (gratis versie) — advertentiemediatie. Zie {appodeal_link}."
            ),
            pl=(
                f"<strong>Appodeal</strong> (wersja darmowa) — mediacja reklamowa. Zobacz {appodeal_link}."
            ),
            zh_CN=(
                f"<strong>Appodeal</strong>（免费版）— 广告中介。可能处理 IP、广告标识符与互动数据。"
                f"详见 {appodeal_link}。"
            ),
            ja=(
                f"<strong>Appodeal</strong>（無料版）— 広告メディエーション。詳細は {appodeal_link}。"
            ),
            ko=(
                f"<strong>Appodeal</strong>(무료 버전) — 광고 미디에이션. 자세한 내용: {appodeal_link}."
            ),
            vi=(
                f"<strong>Appodeal</strong> (bản miễn phí) — trung gian quảng cáo. Xem {appodeal_link}."
            ),
        )),
        t(lang, L(
            en=(
                f"<strong>Google Play Billing</strong> — in-app purchases for PlatePrivacy Pro. Payment and "
                f"purchase records are processed by Google. See {GPLAY}."
            ),
            ru=(
                f"<strong>Google Play Billing</strong> — покупки PlatePrivacy Pro. Платёж обрабатывает Google. "
                f"См. {GPLAY}."
            ),
            uk=(
                f"<strong>Google Play Billing</strong> — покупки PlatePrivacy Pro. Платіж обробляє Google."
            ),
            de=(
                f"<strong>Google Play Billing</strong> — In-App-Käufe für PlatePrivacy Pro. Zahlungen "
                f"verarbeitet Google. Siehe {GPLAY}."
            ),
            fr=(
                f"<strong>Google Play Billing</strong> — achats in-app PlatePrivacy Pro. Paiements traités "
                f"par Google. Voir {GPLAY}."
            ),
            es=(
                f"<strong>Google Play Billing</strong> — compras in-app de PlatePrivacy Pro. Google procesa "
                f"los pagos. Consulte {GPLAY}."
            ),
            it=(
                f"<strong>Google Play Billing</strong> — acquisti in-app PlatePrivacy Pro. I pagamenti sono "
                f"gestiti da Google. Vedi {GPLAY}."
            ),
            pt=(
                f"<strong>Google Play Billing</strong> — compras na app PlatePrivacy Pro. Pagamentos pela "
                f"Google. Ver {GPLAY}."
            ),
            nl=(
                f"<strong>Google Play Billing</strong> — in-app-aankopen PlatePrivacy Pro. Betalingen via "
                f"Google. Zie {GPLAY}."
            ),
            pl=(
                f"<strong>Google Play Billing</strong> — zakupy w aplikacji PlatePrivacy Pro. Płatności "
                f"obsługuje Google. Zobacz {GPLAY}."
            ),
            zh_CN=f"<strong>Google Play Billing</strong> — PlatePrivacy Pro 应用内购买。付款由 Google 处理。详见 {GPLAY}。",
            ja=f"<strong>Google Play Billing</strong> — PlatePrivacy Pro のアプリ内課金。支払いは Google が処理。{GPLAY}",
            ko=f"<strong>Google Play Billing</strong> — PlatePrivacy Pro 인앱 결제. 결제는 Google이 처리. {GPLAY}",
            vi=f"<strong>Google Play Billing</strong> — mua PlatePrivacy Pro trong ứng dụng. Thanh toán do Google xử lý. Xem {GPLAY}.",
        )),
    ]

    third_tail = t(lang, L(
        en="These providers may process data on servers outside your country. Their use of data is governed by their own policies.",
        ru="Эти поставщики могут обрабатывать данные на серверах за пределами вашей страны. Использование данных регулируется их политиками.",
        uk="Ці постачальники можуть обробляти дані на серверах за межами вашої країни.",
        de="Diese Anbieter können Daten auf Servern außerhalb Ihres Landes verarbeiten. Es gelten deren eigene Richtlinien.",
        fr="Ces prestataires peuvent traiter des données hors de votre pays. Leur utilisation est régie par leurs propres politiques.",
        es="Estos proveedores pueden tratar datos fuera de su país. Se rigen por sus propias políticas.",
        it="Questi fornitori possono elaborare dati fuori dal tuo Paese. Valgono le loro policy.",
        pt="Estes fornecedores podem processar dados fora do seu país. Regem-se pelas próprias políticas.",
        nl="Deze aanbieders kunnen gegevens buiten uw land verwerken. Hun eigen beleidsregels gelden.",
        pl="Ci dostawcy mogą przetwarzać dane poza Twoim krajem. Obowiązują ich własne polityki.",
        zh_CN="这些提供商可能在您所在国家/地区以外的服务器上处理数据，并受其各自政策约束。",
        ja="これらの提供者は国外サーバーでデータを処理する場合があります。各社のポリシーが適用されます。",
        ko="이들 제공자는 해외 서버에서 데이터를 처리할 수 있으며 각 정책이 적용됩니다.",
        vi="Các nhà cung cấp này có thể xử lý dữ liệu ngoài quốc gia của bạn theo chính sách riêng của họ.",
    ))

    store1 = t(lang, L(
        en=(
            "Edited files, cache copies, thumbnails, and settings remain on your device until you delete "
            "them, clear app data, or uninstall the app. We do not operate a cloud backup of your media."
        ),
        ru=(
            "Обработанные файлы, кэш, миниатюры и настройки остаются на устройстве, пока вы их не "
            "удалите, не очистите данные приложения или не удалите приложение. Облачного бэкапа медиа "
            "мы не ведём."
        ),
        uk=(
            "Оброблені файли, кеш, мініатюри та налаштування залишаються на пристрої, доки ви їх не "
            "видалите. Хмарного резервного копіювання медіа ми не ведемо."
        ),
        de=(
            "Bearbeitete Dateien, Cache, Vorschaubilder und Einstellungen bleiben auf dem Gerät, bis "
            "Sie sie löschen, App-Daten löschen oder die App deinstallieren. Wir betreiben kein "
            "Cloud-Backup Ihrer Medien."
        ),
        fr=(
            "Fichiers édités, cache, miniatures et réglages restent sur l’appareil jusqu’à suppression "
            "des données ou désinstallation. Nous n’avons pas de sauvegarde cloud de vos médias."
        ),
        es=(
            "Archivos editados, caché, miniaturas y ajustes permanecen en el dispositivo hasta que los "
            "borre o desinstale la app. No hay copia en la nube de sus medios."
        ),
        it=(
            "File modificati, cache, miniature e impostazioni restano sul dispositivo finché non li "
            "elimini o disinstalli l’app. Non gestiamo un backup cloud dei tuoi media."
        ),
        pt=(
            "Ficheiros editados, cache, miniaturas e definições ficam no dispositivo até os apagar ou "
            "desinstalar a app. Não fazemos cópia na nuvem dos seus conteúdos."
        ),
        nl=(
            "Bewerkt bestanden, cache, miniaturen en instellingen blijven op het apparaat tot u ze "
            "verwijdert of de app deïnstalleert. Wij hebben geen cloudback-up van uw media."
        ),
        pl=(
            "Przetworzone pliki, cache, miniatury i ustawienia pozostają na urządzeniu, dopóki ich nie "
            "usuniesz lub nie odinstalujesz aplikacji. Nie prowadzimy kopii w chmurze."
        ),
        zh_CN="编辑后的文件、缓存、缩略图和设置会保留在设备上，直到您删除、清除应用数据或卸载应用。我们不做云端媒体备份。",
        ja="編集済みファイル・キャッシュ・サムネイル・設定は、削除・データ消去・アンインストールまで端末に残ります。メディアのクラウドバックアップはありません。",
        ko="편집된 파일, 캐시, 썸네일, 설정은 삭제·데이터 삭제·앱 삭제 전까지 기기에 남습니다. 미디어 클라우드 백업은 하지 않습니다.",
        vi=(
            "Tệp đã chỉnh, bộ nhớ đệm, ảnh thu nhỏ và cài đặt ở lại trên thiết bị cho đến khi bạn "
            "xóa hoặc gỡ ứng dụng. Chúng tôi không sao lưu đám mây media của bạn."
        ),
    ))
    store2 = t(lang, L(
        en="If you email us for support, we keep your message only as long as needed to handle the request.",
        ru="Если вы пишете нам в поддержку, мы храним сообщение только столько, сколько нужно для ответа.",
        uk="Якщо ви пишете нам у підтримку, ми зберігаємо повідомлення лише стільки, скільки потрібно для відповіді.",
        de="Wenn Sie uns per E-Mail um Support bitten, speichern wir die Nachricht nur so lange wie nötig.",
        fr="Si vous nous écrivez pour le support, nous conservons le message uniquement le temps nécessaire.",
        es="Si nos escribe para soporte, conservamos el mensaje solo el tiempo necesario.",
        it="Se ci scrivi per supporto, conserviamo il messaggio solo per il tempo necessario.",
        pt="Se nos enviar e-mail de suporte, guardamos a mensagem só o tempo necessário.",
        nl="Als u ons mailt voor support, bewaren we het bericht alleen zo lang als nodig.",
        pl="Jeśli napiszesz do nas w sprawie wsparcia, przechowujemy wiadomość tylko tak długo, jak trzeba.",
        zh_CN="若您发邮件寻求支持，我们仅在处理请求所需期间保留该邮件。",
        ja="サポートのためにメールをいただいた場合、対応に必要な期間のみ保存します。",
        ko="지원을 위해 이메일을 보내시면 처리에 필요한 기간만 보관합니다.",
        vi="Nếu bạn gửi email hỗ trợ, chúng tôi chỉ giữ thư trong thời gian cần để xử lý.",
    ))

    sec = t(lang, L(
        en="We use reasonable measures to protect data stored by the app on your device. No method of storage or transmission is 100% secure.",
        ru="Мы применяем разумные меры для защиты данных на устройстве. Ни один способ хранения или передачи не является абсолютно безопасным.",
        uk="Ми застосовуємо розумні заходи для захисту даних на пристрої.",
        de="Wir treffen angemessene Maßnahmen zum Schutz der auf dem Gerät gespeicherten Daten. Keine Methode ist zu 100 % sicher.",
        fr="Nous prenons des mesures raisonnables pour protéger les données sur l’appareil. Aucune méthode n’est sûre à 100 %.",
        es="Adoptamos medidas razonables para proteger los datos en el dispositivo. Ningún método es 100 % seguro.",
        it="Adottiamo misure ragionevoli per proteggere i dati sul dispositivo. Nessun metodo è sicuro al 100%.",
        pt="Adotamos medidas razoáveis para proteger os dados no dispositivo. Nenhum método é 100% seguro.",
        nl="We nemen redelijke maatregelen om gegevens op het apparaat te beschermen. Geen methode is 100% veilig.",
        pl="Stosujemy rozsądne środki ochrony danych na urządzeniu. Żadna metoda nie jest w 100% bezpieczna.",
        zh_CN="我们采取合理措施保护应用在设备上存储的数据。任何存储或传输方式都无法做到百分之百安全。",
        ja="端末上のデータを保護するため合理的な措置を講じます。保存・送信の方法に100%の安全はありません。",
        ko="기기에 저장된 데이터를 보호하기 위해 합리적 조치를 취합니다. 어떤 방식도 100% 안전하지는 않습니다.",
        vi="Chúng tôi dùng biện pháp hợp lý để bảo vệ dữ liệu trên thiết bị. Không phương thức nào an toàn 100%.",
    ))

    child = t(lang, L(
        en="PlatePrivacy is not directed at children under 13 (or the minimum age required in your country). We do not knowingly collect personal information from children.",
        ru="PlatePrivacy не предназначено для детей младше 13 лет (или минимального возраста в вашей стране). Мы сознательно не собираем персональные данные детей.",
        uk="PlatePrivacy не спрямовано на дітей молодше 13 років (або мінімального віку у вашій країні).",
        de="PlatePrivacy richtet sich nicht an Kinder unter 13 (oder dem Mindestalter in Ihrem Land). Wir erheben wissentlich keine Daten von Kindern.",
        fr="PlatePrivacy ne s’adresse pas aux enfants de moins de 13 ans (ou l’âge minimum dans votre pays).",
        es="PlatePrivacy no está dirigido a menores de 13 años (o la edad mínima de su país).",
        it="PlatePrivacy non è rivolto a minori di 13 anni (o all’età minima del tuo Paese).",
        pt="O PlatePrivacy não se destina a menores de 13 anos (ou à idade mínima do seu país).",
        nl="PlatePrivacy is niet gericht op kinderen onder 13 (of de minimumleeftijd in uw land).",
        pl="PlatePrivacy nie jest przeznaczone dla dzieci poniżej 13 lat (lub minimalnego wieku w Twoim kraju).",
        zh_CN="PlatePrivacy 不面向 13 岁以下儿童（或您所在国家/地区要求的最低年龄）。我们不会故意收集儿童的个人信息。",
        ja="PlatePrivacy は 13 歳未満（または各国の最低年齢）の子ども向けではありません。子どもの個人情報を意図的に収集しません。",
        ko="PlatePrivacy는 13세 미만(또는 해당 국가 최소 연령) 아동을 대상으로 하지 않으며, 아동 개인정보를 고의로 수집하지 않습니다.",
        vi="PlatePrivacy không dành cho trẻ dưới 13 tuổi (hoặc độ tuổi tối thiểu tại quốc gia bạn). Chúng tôi không cố ý thu thập thông tin cá nhân của trẻ.",
    ))

    rights1 = t(lang, L(
        en=(
            "Depending on your location (for example the EU/EEA under GDPR), you may have rights to "
            "access, rectify, erase, restrict, or object to processing of personal data, and to lodge "
            "a complaint with a supervisory authority."
        ),
        ru=(
            "В зависимости от вашего местоположения (например, в ЕС/ЕЭЗ по GDPR) у вас могут быть права "
            "на доступ, исправление, удаление, ограничение или возражение против обработки персональных "
            "данных, а также право подать жалобу в надзорный орган."
        ),
        uk=(
            "Залежно від вашого місцезнаходження (наприклад, у ЄС/ЄЕЗ за GDPR) у вас можуть бути права "
            "на доступ, виправлення, видалення, обмеження або заперечення проти обробки персональних даних."
        ),
        de=(
            "Je nach Ihrem Standort (z. B. EU/EWR nach DSGVO) können Sie Rechte auf Auskunft, Berichtigung, "
            "Löschung, Einschränkung oder Widerspruch sowie auf Beschwerde bei einer Aufsichtsbehörde haben."
        ),
        fr=(
            "Selon votre lieu de résidence (par ex. UE/EEE au titre du RGPD), vous pouvez avoir des droits "
            "d’accès, de rectification, d’effacement, de limitation ou d’opposition, et de réclamation "
            "auprès d’une autorité."
        ),
        es=(
            "Según su ubicación (p. ej. UE/EEE bajo el RGPD), puede tener derechos de acceso, "
            "rectificación, supresión, limitación u oposición, y de presentar una reclamación."
        ),
        it=(
            "A seconda della tua ubicazione (es. UE/SEE ai sensi del GDPR), puoi avere diritti di accesso, "
            "rettifica, cancellazione, limitazione o opposizione, e di reclamo a un’autorità."
        ),
        pt=(
            "Consoante a localização (p. ex. UE/EEE ao abrigo do RGPD), pode ter direitos de acesso, "
            "retificação, apagamento, limitação ou oposição, e de apresentar reclamação."
        ),
        nl=(
            "Afhankelijk van uw locatie (bijv. EU/EER onder de AVG) kunt u rechten hebben op inzage, "
            "rectificatie, wissing, beperking of bezwaar, en een klacht indienen bij een toezichthouder."
        ),
        pl=(
            "W zależności od lokalizacji (np. UE/EOG według RODO) możesz mieć prawa dostępu, "
            "sprostowania, usunięcia, ograniczenia lub sprzeciwu oraz skargi do organu nadzorczego."
        ),
        zh_CN=(
            "根据您所在地（例如欧盟/欧洲经济区适用 GDPR），您可能享有访问、更正、删除、限制或反对处理"
            "个人数据的权利，并向监管机构投诉。"
        ),
        ja=(
            "所在地によっては（例：EU/EEA の GDPR）、個人データのアクセス・訂正・消去・制限・異議、"
            "監督機関への苦情申立ての権利がある場合があります。"
        ),
        ko=(
            "소재지(예: GDPR이 적용되는 EU/EEA)에 따라 개인정보 열람·정정·삭제·제한·반대 및 "
            "감독기관 신고 권리가 있을 수 있습니다."
        ),
        vi=(
            "Tùy nơi bạn ở (ví dụ EU/EEA theo GDPR), bạn có thể có quyền truy cập, sửa, xóa, hạn chế "
            "hoặc phản đối xử lý dữ liệu cá nhân, và khiếu nại với cơ quan giám sát."
        ),
    ))
    rights2 = t(lang, L(
        en=(
            f"Because most data stays on your device, you can often exercise these rights by clearing "
            f"app data or uninstalling the app. For advertising-related data, use Android ad settings "
            f"and see the {appodeal_link}. Contact us at {MAIL} for other requests."
        ),
        ru=(
            f"Поскольку большая часть данных остаётся на устройстве, вы часто можете реализовать эти "
            f"права, очистив данные приложения или удалив его. Для рекламы — настройки Android и "
            f"{appodeal_link}. Иное: {MAIL}."
        ),
        uk=(
            f"Оскільки більшість даних залишається на пристрої, ви можете очистити дані застосунку або "
            f"видалити його. З питань реклами — {appodeal_link}. Інше: {MAIL}."
        ),
        de=(
            f"Da die meisten Daten auf dem Gerät bleiben, können Sie Rechte oft durch Löschen der "
            f"App-Daten oder Deinstallation ausüben. Für Werbung: Android-Einstellungen und "
            f"{appodeal_link}. Sonstiges: {MAIL}."
        ),
        fr=(
            f"La plupart des données restent sur l’appareil : effacez les données ou désinstallez. "
            f"Pour la pub : réglages Android et {appodeal_link}. Autre : {MAIL}."
        ),
        es=(
            f"Como la mayoría de datos están en el dispositivo, borre datos o desinstale. Para "
            f"publicidad: ajustes de Android y {appodeal_link}. Otros: {MAIL}."
        ),
        it=(
            f"Poiché la maggior parte dei dati resta sul dispositivo, puoi cancellare i dati o "
            f"disinstallare. Per gli annunci: impostazioni Android e {appodeal_link}. Altro: {MAIL}."
        ),
        pt=(
            f"Como a maioria dos dados fica no dispositivo, limpe os dados ou desinstale. Para anúncios: "
            f"definições Android e {appodeal_link}. Outro: {MAIL}."
        ),
        nl=(
            f"Omdat de meeste gegevens op het apparaat blijven, kunt u app-gegevens wissen of "
            f"deïnstalleren. Voor advertenties: Android-instellingen en {appodeal_link}. Anders: {MAIL}."
        ),
        pl=(
            f"Ponieważ większość danych jest na urządzeniu, często wystarczy wyczyścić dane lub "
            f"odinstalować aplikację. Reklamy: ustawienia Androida i {appodeal_link}. Inne: {MAIL}."
        ),
        zh_CN=(
            f"由于多数数据留在设备上，您通常可通过清除应用数据或卸载来行使权利。广告相关数据请使用 "
            f"Android 广告设置并参阅 {appodeal_link}。其他请求：{MAIL}。"
        ),
        ja=(
            f"データの多くは端末に残るため、アプリデータの消去やアンインストールで権利を行使できることが"
            f"多いです。広告関連は Android の広告設定と {appodeal_link}。その他：{MAIL}。"
        ),
        ko=(
            f"대부분 데이터가 기기에 있으므로 앱 데이터 삭제나 앱 삭제로 권리를 행사할 수 있습니다. "
            f"광고 관련은 Android 광고 설정과 {appodeal_link}. 기타: {MAIL}."
        ),
        vi=(
            f"Vì hầu hết dữ liệu ở trên thiết bị, bạn thường có thể xóa dữ liệu ứng dụng hoặc gỡ app. "
            f"Dữ liệu quảng cáo: cài đặt quảng cáo Android và {appodeal_link}. Khác: {MAIL}."
        ),
    ))

    chg = t(lang, L(
        en=(
            "We may update this policy from time to time. The “Last updated” date at the top will change "
            "when we do. Continued use of the app after changes means you accept the updated policy."
        ),
        ru=(
            "Мы можем обновлять эту политику. Дата «Последнее обновление» изменится при этом. "
            "Продолжение использования приложения означает принятие обновлённой политики."
        ),
        uk=(
            "Ми можемо оновлювати цю політику. Дата «Останнє оновлення» зміниться відповідно."
        ),
        de=(
            "Wir können diese Richtlinie aktualisieren. Das Datum „Zuletzt aktualisiert“ ändert sich "
            "dann. Die weitere Nutzung gilt als Zustimmung."
        ),
        fr=(
            "Nous pouvons mettre à jour cette politique. La date « Dernière mise à jour » changera. "
            "L’utilisation continue vaut acceptation."
        ),
        es=(
            "Podemos actualizar esta política. Cambiará la fecha de «Última actualización». El uso "
            "continuado implica aceptación."
        ),
        it=(
            "Possiamo aggiornare questa informativa. Cambierà la data «Ultimo aggiornamento». "
            "L’uso continuato implica accettazione."
        ),
        pt=(
            "Podemos atualizar esta política. A data «Última atualização» mudará. O uso continuado "
            "implica aceitação."
        ),
        nl=(
            "We kunnen dit beleid bijwerken. De datum «Laatst bijgewerkt» verandert dan. Verder gebruik "
            "geldt als aanvaarding."
        ),
        pl=(
            "Możemy aktualizować tę politykę. Zmieni się data «Ostatnia aktualizacja». Dalsze "
            "korzystanie oznacza akceptację."
        ),
        zh_CN="我们可能不时更新本政策。顶部的“最后更新”日期会随之变更。变更后继续使用即表示接受更新后的政策。",
        ja="本ポリシーは随時更新することがあります。「最終更新」の日付が変わります。変更後の利用は更新への同意とみなします。",
        ko="본 방침은 수시로 업데이트될 수 있으며 «최종 업데이트» 날짜가 변경됩니다. 변경 후 계속 사용하면 동의한 것으로 봅니다.",
        vi=(
            "Chúng tôi có thể cập nhật chính sách. Ngày «Cập nhật lần cuối» sẽ thay đổi. Tiếp tục "
            "dùng ứng dụng sau thay đổi nghĩa là bạn chấp nhận."
        ),
    ))

    contact = t(lang, L(
        en=f"Questions about this policy: {MAIL}",
        ru=f"Вопросы по политике: {MAIL}",
        uk=f"Питання щодо політики: {MAIL}",
        de=f"Fragen zu dieser Richtlinie: {MAIL}",
        fr=f"Questions sur cette politique : {MAIL}",
        es=f"Preguntas sobre esta política: {MAIL}",
        it=f"Domande su questa informativa: {MAIL}",
        pt=f"Perguntas sobre esta política: {MAIL}",
        nl=f"Vragen over dit beleid: {MAIL}",
        pl=f"Pytania dotyczące tej polityki: {MAIL}",
        zh_CN=f"有关本政策的问题：{MAIL}",
        ja=f"本ポリシーに関するお問い合わせ：{MAIL}",
        ko=f"본 방침 관련 문의: {MAIL}",
        vi=f"Câu hỏi về chính sách này: {MAIL}",
    ))

    return {
        "title": t(lang, TITLE),
        "updatedLabel": t(lang, UPDATED),
        "footer": t(lang, FOOTER),
        "fallbackNotice": "",
        "sections": [
            {"title": s_intro, "blocks": [
                {"type": "p", "html": intro1},
                {"type": "p", "html": intro2},
            ]},
            {"title": s_ctrl, "blocks": [
                {"type": "p", "html": ctrl},
            ]},
            {"title": s_info, "blocks": [
                {"type": "p", "html": info_lead},
                {"type": "ul", "items": items_info},
                {"type": "p", "html": info_tail},
            ]},
            {"title": s_perm, "blocks": [
                {"type": "p", "html": perm_lead},
                {"type": "ul", "items": items_perm},
                {"type": "p", "html": perm_tail},
            ]},
            {"title": s_use, "blocks": [
                {"type": "ul", "items": items_use},
            ]},
            {"title": s_third, "blocks": [
                {"type": "p", "html": third_lead},
                {"type": "ul", "items": items_third},
                {"type": "p", "html": third_tail},
            ]},
            {"title": s_store, "blocks": [
                {"type": "p", "html": store1},
                {"type": "p", "html": store2},
            ]},
            {"title": s_sec, "blocks": [
                {"type": "p", "html": sec},
            ]},
            {"title": s_child, "blocks": [
                {"type": "p", "html": child},
            ]},
            {"title": s_rights, "blocks": [
                {"type": "p", "html": rights1},
                {"type": "p", "html": rights2},
            ]},
            {"title": s_chg, "blocks": [
                {"type": "p", "html": chg},
            ]},
            {"title": s_contact, "blocks": [
                {"type": "p", "html": contact},
            ]},
        ],
    }


def main() -> None:
    CONTENT.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        data = build(lang)
        out = CONTENT / f"{lang}.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("wrote", out.name)
    print("done", len(LANGS), "locales")


if __name__ == "__main__":
    main()
