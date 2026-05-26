import json
from pathlib import Path

from django.core.management.base import BaseCommand

from apps.cms.models import Page, PageSection
from apps.franchise.models import FranchiseFAQ
from apps.gallery.models import GalleryImage
from apps.locations.models import Location, OpeningHours
from apps.menu.models import MenuDocument, MenuPageImage
from apps.navigation.models import NavItem
from apps.settings_app.models import SiteSettings


class Command(BaseCommand):
    help = "Seed starter content for 8848 Momo House Germany."

    def _frontend_locale(self, namespace, language):
        backend_root = Path(__file__).resolve().parents[4]
        frontend_root = backend_root.parent / "8848momohousegermany"
        locale_path = frontend_root / "src" / "i18n" / "locales" / language / f"{namespace}.json"
        if not locale_path.exists():
            return {}
        with locale_path.open("r", encoding="utf-8") as locale_file:
            return json.load(locale_file)

    def _seed_page_sections_from_locale(self, slug, title, namespace, section_keys, section_type="content"):
        content_en = self._frontend_locale(namespace, "en")
        content_de = self._frontend_locale(namespace, "nl")
        page, _ = Page.objects.get_or_create(title=title, slug=slug)

        for index, section_key in enumerate(section_keys, start=1):
            section_en = dict(content_en.get(section_key, {}))
            section_de = dict(content_de.get(section_key, {}))
            if section_key == "inquiry":
                section_en["form"] = content_en.get("form", {})
                section_en["email"] = content_en.get("email", {})
                section_de["form"] = content_de.get("form", {})
                section_de["email"] = content_de.get("email", {})

            PageSection.objects.update_or_create(
                page=page,
                section_key=section_key,
                defaults={
                    "section_type": "form" if section_key == "inquiry" else section_type,
                    "order": index * 10,
                    "is_active": True,
                    "content": section_en,
                    "content_en": section_en,
                    "content_de": section_de or section_en,
                },
            )

        return content_en, content_de

    def handle(self, *args, **options):
        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                "site_name": "8848 Momo House Germany",
                "phone": "+496976029152",
                "phone_display": "+49 6976029152",
                "email": "hello@8848momohouse.de",
                "city": "Frankfurt, Germany",
                "address": "Ludwigstrasse 10, 60327 Frankfurt am Main, Germany",
                "opening_hours": "11am - 09pm",
                "facebook_url": "https://www.facebook.com/8848MomoHouseFrankfurt",
                "instagram_url": "https://www.instagram.com/8848momohouse/",
                "youtube_url": "https://www.youtube.com/@momohouse-js7gp",
                "order_url": "https://www.8848momos.com.au/order",
                "privacy_url": "#",
                "terms_url": "#",
                "footer_text": "When you come to 8848 Momo House, expect to feel uplifted and warmly welcomed. Bring your friends, eat and drink and have some laughs. Above all, expect 100% satisfaction.",
            },
        )

        for order, (label, url) in enumerate(
            [
                ("Home", "/"),
                ("Menu", "/menu/"),
                ("Gallery", "/gallery/"),
                ("Events", "#"),
                ("Rewards", "#"),
                ("Stuff", "#"),
                ("Franchise", "/franchise/"),
                ("Careers", "#"),
                ("About Us", "/about-us/"),
            ],
            start=1,
        ):
            NavItem.objects.update_or_create(
                label=label,
                parent=None,
                defaults={"url": url, "order": order * 10, "is_active": True, "open_in_new_tab": False},
            )

        home, _ = Page.objects.get_or_create(title="Home", slug="home")
        PageSection.objects.update_or_create(
            page=home,
            section_key="hero",
            defaults={
                "section_type": "hero",
                "order": 10,
                "is_active": True,
                "content": {
                    "kicker": "NEPALESE RESTAURANT | Germany",
                    "title1": "NEPALESE DUMPLINGS",
                    "title2": "& ORIENTAL FUSION",
                    "desc": "8848 Momo House treats Nepali expats and hungry German diners to a unique Oriental Fusion menu featuring yummy Nepalese momos tender, plump, succulent dumplings stuffed with authentic & innovative tasty fillings.",
                    "ctaMenu": "VIEW MENU",
                    "ctaOrder": "ORDER ONLINE",
                    "orderUrl": "https://www.8848momos.com.au/order",
                    "handImage": "/8848-assets/hand-momo.png",
                    "handAlt": "Hand holding momo",
                    "badgeImage": "/8848-assets/hom-badge.jpeg",
                    "everestTitle": "MOUNT EVEREST",
                    "everestCountry": "Nepal",
                    "everestHeight": "8848m",
                },
                "content_en": {
                    "kicker": "NEPALESE RESTAURANT | Germany",
                    "title1": "NEPALESE DUMPLINGS",
                    "title2": "& ORIENTAL FUSION",
                    "desc": "8848 Momo House treats Nepali expats and hungry German diners to a unique Oriental Fusion menu featuring yummy Nepalese momos tender, plump, succulent dumplings stuffed with authentic & innovative tasty fillings.",
                    "ctaMenu": "VIEW MENU",
                    "ctaOrder": "ORDER ONLINE",
                    "orderUrl": "https://www.8848momos.com.au/order",
                    "handImage": "/8848-assets/hand-momo.png",
                    "handAlt": "Hand holding momo",
                    "badgeImage": "/8848-assets/hom-badge.jpeg",
                    "everestTitle": "MOUNT EVEREST",
                    "everestCountry": "Nepal",
                    "everestHeight": "8848m",
                },
                "content_de": {
                    "kicker": "NEPALESISCHES RESTAURANT | Deutschland",
                    "title1": "NEPALESISCHE DUMPLINGS",
                    "title2": "& ORIENTAL FUSION",
                    "desc": "8848 Momo House begruesst Nepalesen und hungrige Gaeste in Deutschland mit einer einzigartigen Oriental-Fusion-Karte voller koestlicher Momos: zart, saftig und gefuellt mit authentischen und kreativen Aromen.",
                    "ctaMenu": "MENU ANSEHEN",
                    "ctaOrder": "ONLINE BESTELLEN",
                    "orderUrl": "https://www.8848momos.com.au/order",
                    "handImage": "/8848-assets/hand-momo.png",
                    "handAlt": "Hand haelt Momo",
                    "badgeImage": "/8848-assets/hom-badge.jpeg",
                    "everestTitle": "MOUNT EVEREST",
                    "everestCountry": "Nepal",
                    "everestHeight": "8848m",
                },
            },
        )
        PageSection.objects.update_or_create(
            page=home,
            section_key="roots",
            defaults={
                "section_type": "content",
                "order": 30,
                "is_active": True,
                "content": {
                    "imageAlt": "Nepalese roots section",
                    "title1": "NEPALESE ROOTS,",
                    "title2": "AUSSIE INVENTION?",
                    "lead": "8848 Momo House is the invention of Hom Pyashi, Nepali and proud new Aussie.",
                    "body": "Homesick and craving his familiar comfort foods, Hom built a restaurant our Nepalese friends instantly love, and our Aussie mates have discovered as a brand new cuisine thats tickling their tastebuds.",
                    "ctaMenu": "VIEW OUR MENU",
                    "href": "/menu",
                    "image": "/8848-assets/jhol_Momo.png",
                    "badgeImage": "/8848-assets/Eighty-eight-Forty-Eight-Hom-Pyashi-Badge-Colour-Watermark.png",
                    "concreteBackground": "/8848-assets/Concrete-Background.jpg",
                    "columnBackground": "/8848-assets/Column-white-background-grunge.png",
                },
                "content_en": {
                    "imageAlt": "Nepalese roots section",
                    "title1": "NEPALESE ROOTS,",
                    "title2": "AUSSIE INVENTION?",
                    "lead": "8848 Momo House is the invention of Hom Pyashi, Nepali and proud new Aussie.",
                    "body": "Homesick and craving his familiar comfort foods, Hom built a restaurant our Nepalese friends instantly love, and our Aussie mates have discovered as a brand new cuisine thats tickling their tastebuds.",
                    "ctaMenu": "VIEW OUR MENU",
                    "href": "/menu",
                    "image": "/8848-assets/jhol_Momo.png",
                    "badgeImage": "/8848-assets/Eighty-eight-Forty-Eight-Hom-Pyashi-Badge-Colour-Watermark.png",
                    "concreteBackground": "/8848-assets/Concrete-Background.jpg",
                    "columnBackground": "/8848-assets/Column-white-background-grunge.png",
                },
                "content_de": {
                    "imageAlt": "Nepalesische Roots Sektion",
                    "title1": "NEPALESISCHE WURZELN,",
                    "title2": "AUSSIE-ERFINDUNG?",
                    "lead": "8848 Momo House ist die Idee von Hom Pyashi, Nepali und stolzer neuer Aussie.",
                    "body": "Mit Heimweh und Lust auf vertrautes Comfort Food baute Hom ein Restaurant, das nepalesische Freunde sofort lieben und in dem australische Freunde eine neue Kueche entdecken.",
                    "ctaMenu": "UNSER MENU ANSEHEN",
                    "href": "/menu",
                    "image": "/8848-assets/jhol_Momo.png",
                    "badgeImage": "/8848-assets/Eighty-eight-Forty-Eight-Hom-Pyashi-Badge-Colour-Watermark.png",
                    "concreteBackground": "/8848-assets/Concrete-Background.jpg",
                    "columnBackground": "/8848-assets/Column-white-background-grunge.png",
                },
            },
        )
        PageSection.objects.update_or_create(
            page=home,
            section_key="momoste",
            defaults={
                "section_type": "content",
                "order": 20,
                "is_active": True,
                "content": {
                    "plateAlt": "Momos plate",
                    "image": "/8848-assets/momo-brass-bowl.png",
                    "title": "MOMOSTE!",
                    "subtitle": "Good times and tasty food!",
                    "body": "Our oriental fusion menu will surprise and excite your tastebuds. You all find yourself coming back over and over to get another tummy-full of our warmth, hospitality and fun!",
                    "whyTitle": "Why 8848?",
                    "whyBody": "Well, thats the height of the glorious Mt Everest in Nepal, the earth highest mountain above sea level - and what inspires us every day to aim for the highest heights of hospitality.",
                    "noteEmph": "Momoste",
                    "noteRest": "is our tongue-in-cheek spin on Namaste. Expect to hear it a lot around our house.",
                },
                "content_en": {
                    "plateAlt": "Momos plate",
                    "image": "/8848-assets/momo-brass-bowl.png",
                    "title": "MOMOSTE!",
                    "subtitle": "Good times and tasty food!",
                    "body": "Our oriental fusion menu will surprise and excite your tastebuds. You all find yourself coming back over and over to get another tummy-full of our warmth, hospitality and fun!",
                    "whyTitle": "Why 8848?",
                    "whyBody": "Well, thats the height of the glorious Mt Everest in Nepal, the earth highest mountain above sea level - and what inspires us every day to aim for the highest heights of hospitality.",
                    "noteEmph": "Momoste",
                    "noteRest": "is our tongue-in-cheek spin on Namaste. Expect to hear it a lot around our house.",
                },
                "content_de": {
                    "plateAlt": "Momos Teller",
                    "image": "/8848-assets/momo-brass-bowl.png",
                    "title": "MOMOSTE!",
                    "subtitle": "Gute Zeiten und leckeres Essen!",
                    "body": "Unser orientalisches Fusion-Menu ueberrascht und begeistert deine Geschmacksknospen. Du wirst immer wiederkommen fuer eine weitere Portion Waerme, Gastfreundschaft und Spass.",
                    "whyTitle": "Warum 8848?",
                    "whyBody": "8848 ist die Hoehe des Mount Everest in Nepal, des hoechsten Berges der Erde ueber dem Meeresspiegel - und inspiriert uns jeden Tag, Gastfreundschaft auf hoechstem Niveau zu bieten.",
                    "noteEmph": "Momoste",
                    "noteRest": "ist unser humorvoller Dreh auf Namaste. Du wirst es bei uns oft hoeren.",
                },
            },
        )
        PageSection.objects.update_or_create(
            page=home,
            section_key="instagram",
            defaults={
                "section_type": "social",
                "order": 70,
                "is_active": True,
                "content": {
                    "handle": "@8848momohouse",
                    "subtitle": "Nepalese Dumplings & Oriental Fusion",
                    "button_text": "Follow",
                    "profile_image": "/8848-assets/logo-header-crop.png",
                    "profile_alt": "8848 Momo House Instagram",
                },
                "content_en": {
                    "handle": "@8848momohouse",
                    "subtitle": "Nepalese Dumplings & Oriental Fusion",
                    "button_text": "Follow",
                    "profile_image": "/8848-assets/logo-header-crop.png",
                    "profile_alt": "8848 Momo House Instagram",
                },
                "content_de": {
                    "handle": "@8848momohouse",
                    "subtitle": "Nepalesische Dumplings & Oriental Fusion",
                    "button_text": "Folgen",
                    "profile_image": "/8848-assets/logo-header-crop.png",
                    "profile_alt": "8848 Momo House Instagram",
                },
            },
        )
        PageSection.objects.update_or_create(
            page=home,
            section_key="yak_club",
            defaults={
                "section_type": "cta",
                "order": 80,
                "is_active": True,
                "content": {
                    "titlePrefix": "JOIN THE",
                    "titleEmph": "MOMOSTE CLUB",
                    "body": "Join the Momoste Club and we all show you the extra special VIP treatment you deserve. You all be the first to receive event invites, announcements, unique discounts and offers.",
                    "cta": "JOIN FOR FREE",
                    "image": "/8848-assets/yak-footer.png",
                    "imageAlt": "Yak club",
                },
                "content_en": {
                    "titlePrefix": "JOIN THE",
                    "titleEmph": "MOMOSTE CLUB",
                    "body": "Join the Momoste Club and we all show you the extra special VIP treatment you deserve. You all be the first to receive event invites, announcements, unique discounts and offers.",
                    "cta": "JOIN FOR FREE",
                    "image": "/8848-assets/yak-footer.png",
                    "imageAlt": "Yak club",
                },
                "content_de": {
                    "titlePrefix": "WERDE TEIL DES",
                    "titleEmph": "MOMOSTE CLUB",
                    "body": "Werde Mitglied im Momoste Club und erhalte die besondere VIP-Behandlung, die du verdienst. Du bekommst zuerst Einladungen zu Events, Neuigkeiten, besondere Rabatte und Angebote.",
                    "cta": "KOSTENLOS BEITRETEN",
                    "image": "/8848-assets/yak-footer.png",
                    "imageAlt": "Yak Club",
                },
            },
        )
        PageSection.objects.update_or_create(
            page=home,
            section_key="updates",
            defaults={
                "section_type": "updates",
                "order": 50,
                "is_active": True,
                "content": {
                    "title": "Follow us for regular update",
                    "readMore": "Read more",
                    "showLess": "Show Less",
                    "posts": [
                        {
                            "key": "newMenu",
                            "title": "New menu now available instore!",
                            "excerpt": "We are very pleased to announce the arrive of our brand new menu! It's momolicious...",
                            "img": "/8848-assets/post-menu.png",
                            "href": "/menu",
                        },
                        {
                            "key": "expandEurope",
                            "title": "Expanding to Europe",
                            "excerpt": "8848 Momo House is now taking its authentic flavours beyond Australia. The taste of Nepal is heading to Europe.",
                            "img": "/8848-assets/post-europe.jpg",
                            "href": "#",
                        },
                        {
                            "key": "perth",
                            "title": "Momo in Perth",
                            "excerpt": "8848 Momo house perth Perth, we are getting closer. 8848 Momo House is officially coming to Victoria Park this May 2026, bringing the Taste of Nepal",
                            "img": "/8848-assets/post-perth.png",
                            "href": "#",
                        },
                    ],
                },
                "content_en": {
                    "title": "Follow us for regular update",
                    "readMore": "Read more",
                    "showLess": "Show Less",
                    "posts": [
                        {
                            "key": "newMenu",
                            "title": "New menu now available instore!",
                            "excerpt": "We are very pleased to announce the arrive of our brand new menu! It's momolicious...",
                            "img": "/8848-assets/post-menu.png",
                            "href": "/menu",
                        },
                        {
                            "key": "expandEurope",
                            "title": "Expanding to Europe",
                            "excerpt": "8848 Momo House is now taking its authentic flavours beyond Australia. The taste of Nepal is heading to Europe.",
                            "img": "/8848-assets/post-europe.jpg",
                            "href": "#",
                        },
                        {
                            "key": "perth",
                            "title": "Momo in Perth",
                            "excerpt": "8848 Momo house perth Perth, we are getting closer. 8848 Momo House is officially coming to Victoria Park this May 2026, bringing the Taste of Nepal",
                            "img": "/8848-assets/post-perth.png",
                            "href": "#",
                        },
                    ],
                },
                "content_de": {
                    "title": "Folge uns fuer regelmaessige Updates",
                    "readMore": "Mehr lesen",
                    "showLess": "Weniger anzeigen",
                    "posts": [
                        {
                            "key": "newMenu",
                            "title": "Neues Menu jetzt im Restaurant verfuegbar!",
                            "excerpt": "Wir freuen uns sehr, unser brandneues Menu anzukuendigen. Es ist momolicious...",
                            "img": "/8848-assets/post-menu.png",
                            "href": "/menu",
                        },
                        {
                            "key": "expandEurope",
                            "title": "Expansion nach Europa",
                            "excerpt": "8848 Momo House bringt seine authentischen Aromen nun ueber Australien hinaus. Der Geschmack Nepals kommt nach Europa.",
                            "img": "/8848-assets/post-europe.jpg",
                            "href": "#",
                        },
                        {
                            "key": "perth",
                            "title": "Momo in Perth",
                            "excerpt": "8848 Momo House Perth, wir kommen naeher. 8848 Momo House kommt im Mai 2026 offiziell nach Victoria Park und bringt den Geschmack Nepals.",
                            "img": "/8848-assets/post-perth.png",
                            "href": "#",
                        },
                    ],
                },
            },
        )

        franchise_content_en, _ = self._seed_page_sections_from_locale(
            "franchise",
            "Franchise",
            "franchise",
            [
                "hero",
                "stats",
                "banner",
                "story",
                "why",
                "formats",
                "support",
                "investment",
                "process",
                "testimonial",
                "faq",
                "inquiry",
            ],
        )

        self._seed_page_sections_from_locale(
            "about",
            "About Us",
            "about",
            ["hero", "splitIntro", "hom", "story"],
        )

        menu_document, _ = MenuDocument.objects.get_or_create(
            slug="germany-menu",
            defaults={
                "title": "Dining & Takeaway Menu",
                "kicker": "8848 MOMO HOUSE - GERMANY",
                "subtitle": "A premium editorial experience blending Nepalese warmth with modern luxury. Scroll to explore our full menu in immersive detail.",
                "lightbox_title": "8848 Momo House - Germany",
                "lightbox_description": "Premium Nepalese fusion menu",
                "footer_title": "8848 Momo House - Germany",
                "footer_subtitle": "Premium Nepalese fusion - Modern editorial dining experience",
                "is_default": True,
                "order": 10,
            },
        )
        for index, image_url in enumerate(
            [
                "/8848-assets/8848 germany qsr menu_page-0001.jpg",
                "/8848-assets/8848 germany qsr menu_page-0002.jpg",
                "/8848-assets/8848 germany qsr menu_page-0003.jpg",
                "/8848-assets/8848 germany qsr menu_page-0004.jpg",
            ],
            start=1,
        ):
            MenuPageImage.objects.get_or_create(
                document=menu_document,
                order=index * 10,
                defaults={
                    "external_image_url": image_url,
                    "alt_text": f"8848 Momo House menu page {index}",
                    "title": f"Menu page {index}",
                    "description": "Premium Nepalese fusion menu",
                },
            )

        gallery_images = [
            ("/gallery/617644782_1299501648874857_563777570824911312_n.jpg", "Authentic Himalayan Flavors", 0),
            ("/gallery/689672756_18075866372378582_4748471350885885049_n.jpg", "Crafted With Tradition", 2),
            ("/gallery/682083582_18073447619378582_4201470612714727230_n.jpg", "Elevated Dining Experience", 1),
            ("/gallery/683844009_18074008022378582_6744251658218158524_n.jpg", "Signature Franchise Ambience", 0),
            ("/gallery/690913600_1391357303022624_306986777952760570_n.jpg", "Freshly Prepared Daily", 2),
            ("/gallery/699905803_1395674515924236_8862937895640454602_n.jpg", "The Taste of the Himalayas", 1),
            ("/gallery/659653523_1363583049133383_5294780339634034547_n.jpg", "Premium Restaurant Experience", 2),
            ("/gallery/663309908_1363583052466716_2927746911495968980_n.jpg", "Modern Himalayan Interior", 0),
            ("/gallery/657818651_1361001296058225_7780074548649079592_n.jpg", "Every Detail Matters", 1),
            ("/gallery/659052232_1361001319391556_8113592981594270841_n.jpg", "A Warm Dining Atmosphere", 0),
            ("/gallery/658042542_1360998722725149_3188214951558336334_n.jpg", "Luxury Meets Tradition", 2),
            ("/gallery/514522482_1138513781640312_928824356955485501_n.jpg", "Curated Culinary Moments", 1),
            ("/gallery/515503401_1138293954995628_4231813753025719888_n.jpg", "Authenticity in Every Bite", 2),
            ("/gallery/493703598_1097963899028634_7754026072028280047_n.jpg", "Inspired by Himalayan Culture", 0),
            ("/gallery/630831463_1317107637114258_4769852074049037717_n.jpg", "Beautifully Crafted Spaces", 1),
            ("/gallery/649925123_1342420134583008_7241311262784313452_n.jpg", "Experience the Summit", 0),
            ("/gallery/667210978_1365141555644199_8043924957435588798_n.jpg", "Moments Worth Sharing", 2),
            ("/gallery/660275657_1363841442440877_1508218509033431157_n.jpg", "Tradition Reimagined", 1),
            ("/gallery/635010081_932313339310448_4999394022787579775_n.jpg", "Premium Hospitality", 0),
            ("/gallery/635235810_934031489138633_4034975548481698592_n.jpg", "Flavors Above Expectations", 2),
            ("/gallery/679528802_987160163825765_2976338946044117438_n.jpg", "Designed for Memorable Gatherings", 1),
            ("/gallery/679051057_988014597073655_3559615886381215986_n.jpg", "Refined Himalayan Dining", 0),
            ("/gallery/679994087_1379560484202306_6412673578865363964_n.jpg", "Where Culture Meets Cuisine", 2),
            ("/gallery/657364644_1360998956058459_481425256782942273_n.jpg", "Authentic Himalayan Dining", 0),
            ("/gallery/661312277_1360998152725206_2387943504577623895_n.jpg", "Crafted Culinary Moments", 2),
            ("/gallery/650619506_1345266560965032_6862016175277555941_n.jpg", "The Taste of the Himalayas", 1),
            ("/gallery/658827015_1359086639583024_1585698037278279405_n.jpg", "Elevated Restaurant Experience", 0),
            ("/gallery/657763472_1360998326058522_6156070505580579085_n.jpg", "Luxury Meets Tradition", 2),
            ("/gallery/660822584_1360998192725202_277411545268006583_n.jpg", "Inspired by Himalayan Culture", 1),
            ("/gallery/657346158_1360998829391805_7784036709851637162_n.jpg", "Premium Dining Atmosphere", 2),
            ("/gallery/658942206_1360998986058456_4729231746235759090_n.jpg", "Every Detail Curated", 0),
            ("/gallery/658012456_1360999059391782_3542414904991694057_n.jpg", "Modern Himalayan Interior", 1),
            ("/gallery/660606523_1360999206058434_2067406470089766344_n.jpg", "Curated Guest Experience", 0),
            ("/gallery/658297334_1360999252725096_3023324195421215656_n.jpg", "Warm Himalayan Welcome", 2),
            ("/gallery/660705672_1360999326058422_7649937306138062630_n.jpg", "Designed for Gatherings", 1),
            ("/gallery/571129961_843411921533924_353649833585970143_n.jpg", "Experience the Summit", 2),
            ("/gallery/581674475_859617753246674_9211006937216067306_n.jpg", "Authenticity in Every Bite", 0),
            ("/gallery/571353822_849523417589441_3169294274818382416_n.jpg", "The Art of Flavor", 1),
            ("/gallery/576804468_855343500340766_8602820587857597555_n.jpg", "Beautifully Crafted Spaces", 0),
            ("/gallery/573872141_853647590510357_1634949583157372937_n.jpg", "Tradition Reimagined", 2),
            ("/gallery/590716561_871212105420572_8498077945170908908_n.jpg", "Moments Worth Sharing", 1),
            ("/gallery/584909102_867349889140127_3367125591766371085_n.jpg", "Premium Hospitality", 0),
            ("/gallery/585194569_866609359214180_1510164762163656183_n.jpg", "Where Culture Meets Cuisine", 2),
        ]
        for index, (image_url, caption, depth) in enumerate(gallery_images, start=1):
            GalleryImage.objects.update_or_create(
                external_image_url=image_url,
                defaults={
                    "caption": caption,
                    "alt_text": f"8848 Momo House gallery image {index}",
                    "depth": depth,
                    "order": index * 10,
                    "is_featured": image_url.endswith("667210978_1365141555644199_8043924957435588798_n.jpg"),
                    "is_active": True,
                },
            )

        for index, faq in enumerate(franchise_content_en.get("faq", {}).get("items", []), start=1):
            FranchiseFAQ.objects.update_or_create(
                question=faq.get("q", "Franchise question"),
                defaults={
                    "answer": faq.get("a", ""),
                    "order": index * 10,
                    "is_active": True,
                },
            )

        location, _ = Location.objects.get_or_create(
            slug="germany",
            defaults={"name": "8848 Momo House Germany", "address": "Germany", "city": "Germany", "country": "Germany"},
        )
        for day in range(7):
            OpeningHours.objects.get_or_create(location=location, day_of_week=day, defaults={"is_closed": True})

        self.stdout.write(self.style.SUCCESS("Seeded starter CMS content."))
