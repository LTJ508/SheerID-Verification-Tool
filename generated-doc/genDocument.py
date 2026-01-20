import sys
import time
import random
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ Error: Pillow required. Install: pip install Pillow")
    sys.exit(1)


def generate_transcript(first: str, last: str, school: str, dob: str):
    """Generate fake academic transcript (higher success rate)"""
    w, h = 850, 1100
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    try:
        font_header = ImageFont.truetype("arial.ttf", 32)
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_text = ImageFont.truetype("arial.ttf", 16)
        font_bold = ImageFont.truetype("arialbd.ttf", 16)
    except:
        font_header = font_title = font_text = font_bold = ImageFont.load_default()
    
    # 1. Header
    draw.text((w//2, 50), school.upper(), fill=(0, 0, 0), font=font_header, anchor="mm")
    draw.text((w//2, 90), "OFFICIAL ACADEMIC TRANSCRIPT", fill=(50, 50, 50), font=font_title, anchor="mm")
    draw.line([(50, 110), (w-50, 110)], fill=(0, 0, 0), width=2)
    
    # 2. Student Info
    y = 150
    draw.text((50, y), f"Student Name: {first} {last}", fill=(0, 0, 0), font=font_bold)
    draw.text((w-300, y), f"Student ID: {random.randint(10000000, 99999999)}", fill=(0, 0, 0), font=font_text)
    y += 30
    draw.text((50, y), f"Date of Birth: {dob}", fill=(0, 0, 0), font=font_text)
    draw.text((w-300, y), f"Date Issued: {time.strftime('%Y-%m-%d')}", fill=(0, 0, 0), font=font_text)
    y += 40
    
    # 3. Current Enrollment Status
    draw.rectangle([(50, y), (w-50, y+40)], fill=(240, 240, 240))
    draw.text((w//2, y+20), "CURRENT STATUS: ENROLLED (SPRING 2026)", fill=(0, 100, 0), font=font_bold, anchor="mm")
    y += 70
    
    # 4. Courses
    courses = [
        ("CS 101", "Intro to Computer Science", "4.0", "A"),
        ("MATH 201", "Calculus I", "3.0", "A-"),
        ("ENG 102", "Academic Writing", "3.0", "B+"),
        ("PHYS 150", "Physics for Engineers", "4.0", "A"),
        ("HIST 110", "World History", "3.0", "A")
    ]
    
    # Table Header
    draw.text((50, y), "Course Code", font=font_bold, fill=(0,0,0))
    draw.text((200, y), "Course Title", font=font_bold, fill=(0,0,0))
    draw.text((600, y), "Credits", font=font_bold, fill=(0,0,0))
    draw.text((700, y), "Grade", font=font_bold, fill=(0,0,0))
    y += 20
    draw.line([(50, y), (w-50, y)], fill=(0, 0, 0), width=1)
    y += 20
    
    for code, title, cred, grade in courses:
        draw.text((50, y), code, font=font_text, fill=(0,0,0))
        draw.text((200, y), title, font=font_text, fill=(0,0,0))
        draw.text((600, y), cred, font=font_text, fill=(0,0,0))
        draw.text((700, y), grade, font=font_text, fill=(0,0,0))
        y += 30
    
    y += 20
    draw.line([(50, y), (w-50, y)], fill=(0, 0, 0), width=1)
    y += 30
    
    # 5. Summary
    draw.text((50, y), "Cumulative GPA: 3.85", font=font_bold, fill=(0,0,0))
    draw.text((w-300, y), "Academic Standing: Good", font=font_bold, fill=(0,0,0))
    
    # 6. Watermark / Footer
    draw.text((w//2, h-50), "This document is electronically generated and valid without signature.", fill=(100, 100, 100), font=font_text, anchor="mm")

    # save image locally
    img.save(f"{school}_{first}_{last}_transcript.png")

def generate_student_id(first: str, last: str, school: str):
    """Generate fake student ID card (Improved)"""
    w, h = 650, 400
    # Randomize background color slightly
    bg_color = (random.randint(240, 255), random.randint(240, 255), random.randint(240, 255))
    img = Image.new("RGB", (w, h), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font_lg = ImageFont.truetype("arial.ttf", 26)
        font_md = ImageFont.truetype("arial.ttf", 18)
        font_sm = ImageFont.truetype("arial.ttf", 14)
        font_bold = ImageFont.truetype("arialbd.ttf", 20)
    except:
        font_lg = font_md = font_sm = font_bold = ImageFont.load_default()
    
    # Header color based on school name hash to be consistent but varied
    header_color = (random.randint(0, 50), random.randint(0, 50), random.randint(50, 150))
    
    draw.rectangle([(0, 0), (w, 80)], fill=header_color)
    draw.text((w//2, 40), school.upper(), fill=(255, 255, 255), font=font_lg, anchor="mm")
    
    # Photo placeholder
    draw.rectangle([(30, 100), (160, 280)], outline=(100, 100, 100), width=2, fill=(220, 220, 220))
    draw.text((95, 190), "PHOTO", fill=(150, 150, 150), font=font_md, anchor="mm")
    
    # Info
    x_info = 190
    y = 110
    draw.text((x_info, y), f"{first} {last}", fill=(0, 0, 0), font=font_bold)
    y += 40
    draw.text((x_info, y), "Student ID:", fill=(100, 100, 100), font=font_sm)
    draw.text((x_info + 80, y), str(random.randint(10000000, 99999999)), fill=(0, 0, 0), font=font_md)
    y += 30
    draw.text((x_info, y), "Role:", fill=(100, 100, 100), font=font_sm)
    draw.text((x_info + 80, y), "Student", fill=(0, 0, 0), font=font_md)
    y += 30
    draw.text((x_info, y), "Valid Thru:", fill=(100, 100, 100), font=font_sm)
    draw.text((x_info + 80, y), f"05/{int(time.strftime('%Y'))+1}", fill=(0, 0, 0), font=font_md)
    
    # Barcode strip
    draw.rectangle([(0, 320), (w, 380)], fill=(255, 255, 255))
    for i in range(40):
        x = 50 + i * 14
        if random.random() > 0.3:
            draw.rectangle([(x, 330), (x+8, 370)], fill=(0, 0, 0))
            
    #save image locally
    img.save(f"{school}_{first}_{last}_student_id.png")

first_name = "Dee Dee"
last_name = "Vaughan"
school_name = "Pennsylvania State University-Main Campus"
dob = "2003-11-06"

generate_transcript(first=first_name, last=last_name, school=school_name, dob=dob)
generate_student_id(first=first_name, last=last_name, school=school_name)