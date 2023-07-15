# تمرین اول
-------
گزارش
-------

# Git برای پروژه مدیریت لیست کارها (To-Do List Manager)


## دستور Git Status

دستور `git status` برای مشاهده وضعیت فعلی پروژه در مخزن Git استفاده می‌شود. این دستور نشان می‌دهد کدام فایل‌ها اصلاح شده، اضافه شده یا حذف شده‌اند و آیا این تغییرات برای commit شدن آماده هستند یا خیر.

## دستور Git Commit

دستور `git commit` برای ذخیره تغییرات در مخزن استفاده می‌شود. با استفاده از گزینه `-m`، کاربر می‌تواند پیام commit را شامل توضیحی درباره تغییراتی که اعمال شده‌اند، درج کند.

## دستور Git Pull

دستور `git pull` برای دریافت و ادغام تغییرات از یک مخزن از راه دور به مخزن محلی استفاده می‌شود. این دستور معمولاً برای به‌روزرسانی مخزن محلی با تغییراتی که توسط اعضای دیگر تیم ایجاد شده‌اند، استفاده می‌شود.

## دستور Git Push

دستور `git push` برای آپلود تغییرات مخزن محلی به یک مخزن از راه دور استفاده می‌شود. این دستور معمولاً برای به اشتراک گذاری تغییراتی که توسط کاربر با سایر اعضای تیم ایجاد شده‌اند، استفاده می‌شود.

## دستور Git Merge

دستور `git merge` برای ترکیب تغییرات از دو یا چند شاخه به یک شاخه استفاده می‌شود. این دستور برای ادغام تغییرات اعضای دیگر تیم با شاخه محلی کاربر استفاده می‌شود.

## دستور Git Checkout

دستور `git checkout` برای تغییر شاخه‌ها یا commit های مختلف در مخزن استفاده می‌شود. این دستور معمولاً برای تغییر به یک شاخه مختلف برای کار بر روی یک قابلیت جدید یا رفع باگ استفاده می‌شود.

## دستور Git Branch

دستور `git branch` برای مدیریت شاخه‌ها در مخزن استفاده می‌شود. این دستور برای ایجاد، تغییر نام یا حذف شاخه‌ها در مخزن استفاده می‌شود.


---------
به طور خلاصه روال انجام به صورت زیر است:

1. با استفاده از دستور `git clone`، مخزن را از مخزن اصلی به دستگاه محلی کلون می کنیم.
2. با استفاده از دستور `git checkout -b` یک شاخه جدید برای قابلیت جدید یا رفع باگ ایجاد مکنیم.
3. تغییرات را در فایل‌های پروژه اعمال کرده و با استفاده از دستور `git add` تغییرات را برای انجام commit آماده می کنیم.
4. با استفاده از دستور `git commit -m` تغییرات را commit می کنیم.
5. با استفاده از دستور `git pull` تغییرات از مخزن اصلی را برای به‌روزرسانی مخزن محلی دریافت می کنیم.
6. در صورت بروز هرگونه تداخل در هنگام pull، تداخل را برطرف می کنیم.
7. با استفاده از دستور `git push` تغییرات را به مخزن اصلی ارسال می کنیم.
8. یک درخواست pull برای ادغام تغییرات با شاخه اصلی ایجاد می کنیم.
9. درخواست pull را بررسی و تأیید می کنیم.
10. با استفاده از دستور `git merge` تغییرات را با شاخه اصلی ادغام می کنیم.
