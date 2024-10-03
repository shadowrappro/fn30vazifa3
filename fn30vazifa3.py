# gitga ulash muvaffaqiyatli amalga oshirildi

foydalanuvchi_string = input("Iltimos, biror matn kiriting: ")

try:
    if not foydalanuvchi_string.isalpha():
        raise ValueError("Kiritilgan stringda faqat harflar bo'lishi kerak.")
    
    print("Kiritilgan string to'g'ri: faqat harflardan iborat.")

except ValueError as e:
    print(f"xato: {e}")

# kodni joylash muvaffaqiyatli tugadi

# kodni git hubga yuborishni amalga oshiramiz