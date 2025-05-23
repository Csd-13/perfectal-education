# Perfectal Education - دليل التشغيل الشامل

Perfectal Education - دليل التشغيل الشامل

1. الإعداد العام:

    المتطلبات الأساسية:
        Git
        Flutter SDK
        Android Studio / Xcode
        Node.js
        Python 3.8+
        Rust toolchain
        Firebase CLI
    استنساخ المستودع:
    Bash

    git clone <https://github.com/perfectal-education/perfectal-app.git>
    cd perfectal-education

2. إعداد الاعتماديات:

    Flutter:
    Bash

cd mobile/flutter
flutter pub get

Python:
Bash

cd ../../python
pip install -r requirements.txt

Rust:
Bash

cd ../rust
cargo build

Firebase:
Bash

    cd ../backend/firebase
    firebase init

        اتبع تعليمات Firebase CLI لإعداد مشروعك.

3. إعداد بيئة التطوير:

    تشغيل برنامج الإعداد:
    Bash

    cd ../../scripts
    ./setup_development.sh

        هذا البرنامج النصي قد يقوم بإعداد متغيرات البيئة، أو تشغيل بعض الخدمات المحلية، أو إجراء عمليات إعداد أخرى. يرجى مراجعة محتواه لمعرفة التفاصيل.

4. تشغيل المكونات:

    Web:
        انتقل إلى web/.
        افتح index.html في متصفحك.
        إذا كانت هناك خدمات خلفية أو JavaScript ديناميكي، فقد تحتاج إلى خادم محلي (مثل http-server أو Python's http.server).
    Flutter (Android/iOS):
        انتقل إلى mobile/flutter/.
        تشغيل التطبيق:
            Android: flutter run -d android
            iOS: flutter run -d ios
        تأكد من إعداد Android Studio/Xcode بشكل صحيح.
    Android (Native):
        افتح مشروع Android Studio في mobile/android/.
        قم ببناء وتشغيل التطبيق باستخدام Android Studio.
    iOS (Native):
        افتح مشروع Xcode في mobile/ios/.
        قم ببناء وتشغيل التطبيق باستخدام Xcode.
    Python Backend:
        انتقل الى مجلد python/.
        قم بتفعيل البيئة الافتراضية.
        تأكد من إعداد قواعد البيانات و متغيرات ال API.
        قم بتشغيل السيرفر.
    Rust Backend:
        انتقل الى مجلد rust/.
        قم بتشغيل الأمر cargo run.
        تأكد من إعداد قواعد البيانات و متغيرات ال API.

5. ملاحظات إضافية:

    Docker: إذا كنت تستخدم Docker، راجع ملفات Dockerfile و docker-compose.yml في جذر المشروع.
    قواعد البيانات: قم بإعداد قواعد البيانات المحددة في ملفات الإعداد (Firebase، قواعد بيانات مخصصة).
    متغيرات البيئة: قم بتكوين متغيرات البيئة اللازمة لمفاتيح API، وقواعد البيانات، وغيرها من الإعدادات.
    التوطين: انتبه إلى متطلبات الخطوط الخاصة باللغات المختلفة (Naskh للعربية، Tifinagh للتامازيغت).
    المساهمة: راجع إرشادات المساهمة في docs/developer_guide/contribution.md.

6. هيكل المشروع:

    mobile/: كود تطبيق الهاتف المحمول (Android، iOS، Flutter).
    web/: واجهة تطبيق الويب.
    backend/: خدمات الخلفية وواجهة برمجة التطبيقات (API).
    python/: وحدات الذكاء الاصطناعي والخدمات المستندة إلى Python.
    rust/: مكونات Rust عالية الأداء.
    design/: أصول التصميم ونماذج واجهة المستخدم.
    localization/: ملفات اللغة.
    docs/: الوثائق.
    scripts/: البرامج النصية المساعدة.
    web/components/sidebar.html: الشريط الجانبي لواجهة الويب.
    web/components/notification_panel.html: لوحة الإشعارات.

آمل أن يكون هذا الدليل شاملاً ومفيدًا.
  p e r f e c t a l _ e d u c a t i o n    
 # perfectal_education
# perfectal_education
# perfectal-education
