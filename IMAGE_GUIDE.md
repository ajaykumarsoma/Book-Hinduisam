# 📸 Image Guide for Chapter 1: Prāṇa Pratiṣṭhā

This guide helps you add images to the chapter. There are **5 image placeholders** that need to be replaced with actual image URLs.

---

## 🎯 Quick Start

### Option 1: Use AI Image Generation (DALL-E, Midjourney, Stable Diffusion)

See **detailed prompts** below for each image.

### Option 2: Search for Existing Images

See **search strings** below for each image location.

### Option 3: Use Your Own Photos

Upload to any image host (Imgur, Google Drive, etc.) and get a direct link.

---

## 📋 The 5 Image Placeholders

### **IMAGE 1: Meenakshi Temple Gopuram**

**Location in file:** Line 10-13  
**Current placeholder:** `IMAGE_URL_1`

**AI Generation Prompt:**
```
Majestic Meenakshi Amman Temple gopuram in Madurai, South India. 
Towering colorful temple tower (gopuram) with thousands of carved Hindu 
deity sculptures in vibrant colors - red, yellow, green, blue. 
Intricate Dravidian architecture, multiple tiers, pyramid shape. 
Clear blue sky background. Photorealistic, architectural photography, 
wide angle, dramatic perspective from ground looking up. 8K quality.
```

**Search Strings:**
- Google Images: `"Meenakshi temple Madurai gopuram" high resolution`
- Wikimedia Commons: `Madurai Meenakshi temple tower`
- Flickr: `Meenakshi Amman temple gopuram creative commons`
- Unsplash: `Hindu temple tower India`

---

### **IMAGE 2: Hindu Temple Fire Ritual (Homa)**

**Location in file:** Line 26-29  
**Current placeholder:** `IMAGE_URL_2`

**AI Generation Prompt:**
```
Hindu priest performing sacred fire ritual (homa/havan) in temple. 
Elderly priest with traditional white dhoti and sacred thread (janeu), 
sitting cross-legged before ceremonial fire pit (kund). Flames rising, 
smoke swirling. Priest pouring ghee into fire with wooden spoon. 
Copper vessels, flowers, incense nearby. Warm golden lighting from fire. 
Temple interior background with oil lamps. Respectful, reverent atmosphere. 
Photorealistic, documentary style. 4K quality.
```

**Search Strings:**
- Google Images: `"Hindu homa ritual" priest fire ceremony`
- Wikimedia Commons: `Havan yajna fire ritual priest`
- Pexels: `Hindu fire ceremony puja`
- Getty Images: `Hindu priest performing homa`

---

### **IMAGE 3: Bronze Ganesha Murti**

**Location in file:** Line 496-499  
**Current placeholder:** `IMAGE_URL_3`

**AI Generation Prompt:**
```
Ancient bronze Ganesha statue, panchaloha metal (five-metal alloy). 
Elephant-headed deity sitting in lalitasana pose. Four arms holding: 
broken tusk, modaka (sweet), axe, lotus. Intricate details - jewelry, 
crown, sacred thread. Warm bronze patina, aged appearance. Museum quality 
sculpture on pedestal. Soft studio lighting highlighting surface texture. 
Clean background. Close-up perspective showing craftsmanship. 
Photorealistic, museum photography. 8K quality.
```

**Search Strings:**
- Google Images: `"bronze Ganesha statue" panchaloha museum quality`
- Wikimedia Commons: `Bronze Ganesh sculpture India`
- Met Museum: `Ganesha bronze India medieval`
- Smithsonian: `South Indian bronze Ganesha`

---

### **IMAGE 4: Shiva Lingam with Abhishekam**

**Location in file:** Line 861-864  
**Current placeholder:** `IMAGE_URL_4`

**AI Generation Prompt:**
```
Shiva Lingam in temple sanctum with water abhishekam (ritual bathing). 
Black granite cylindrical Shiva linga on circular yoni base (pedestal). 
Clear water continuously flowing over the lingam from brass pot above. 
Wet surface reflecting light. Fresh bilva leaves, flowers placed on yoni. 
Small oil lamps (diyas) around the base. Dark stone temple interior, 
atmospheric lighting. Sacred, meditative ambiance. Photorealistic, 
close-up perspective. 4K quality.
```

**Search Strings:**
- Google Images: `"Shiva lingam" abhishekam water temple`
- Wikimedia Commons: `Shiva linga abhisheka ritual`
- Flickr: `Shivalinga temple water pouring`
- Pinterest: `Shiva lingam abhishekam close up`

---

### **IMAGE 5: Tirupati Venkateswara Temple**

**Location in file:** Line 1194-1197  
**Current placeholder:** `IMAGE_URL_5`

**AI Generation Prompt:**
```
Tirupati Venkateswara Temple gopuram (temple tower) on sacred Tirumala hills, 
Andhra Pradesh, India. Massive golden-plated gopuram reaching skyward. 
Dravidian temple architecture with intricate carvings. Temple complex on 
hilltop surrounded by lush green Eastern Ghats mountains. Pilgrims visible 
at entrance for scale. Early morning golden light. Majestic, awe-inspiring 
composition. Photorealistic, architectural photography, wide angle. 
8K quality, dramatic clouds.
```

**Search Strings:**
- Google Images: `"Tirupati temple" Venkateswara gopuram golden`
- Wikimedia Commons: `Tirumala Venkateswara temple Andhra Pradesh`
- Flickr: `Tirupati Balaji temple hills creative commons`
- Tourism sites: `Tirupati temple high resolution official`

---

## 🔧 How to Add Images (Step-by-Step)

### Method 1: Upload to Imgur (Easiest)

1. **Get/Generate your image**
2. Go to: https://imgur.com/upload
3. Upload image (drag & drop)
4. **Right-click** the uploaded image → **Copy image address**
5. URL will look like: `https://i.imgur.com/ABC123.jpg`
6. **Edit the chapter file:** `docs/chapters/chapter_01_prana_pratishtha.md`
7. Find `IMAGE_URL_1` (or 2, 3, 4, 5)
8. Replace with your URL: `![Meenakshi Temple](https://i.imgur.com/ABC123.jpg)`
9. Save file
10. Commit and push to GitHub

### Method 2: Use Direct URLs (Wikimedia Commons, Flickr)

1. Find image on Wikimedia Commons
2. Click image → Click "More details"
3. Copy **"Original file"** URL
4. Replace placeholder in markdown file
5. Commit and push

### Method 3: Use docs/assets Folder (Self-Hosted)

1. Place image in: `Book-Hinduisam/docs/assets/`
2. Name it: `meenakshi_temple.jpg`
3. In markdown, use relative path:
   ```markdown
   ![Meenakshi Temple](../assets/meenakshi_temple.jpg)
   ```
4. Commit both the image and markdown file
5. Push to GitHub

---

## ✅ Verification

After adding images, verify they work:

### Local Preview:
```bash
cd Book-Hinduisam
mkdocs serve
```
Open: http://127.0.0.1:8000/Book-Hinduisam/chapters/chapter_01_prana_pratishtha/

### GitHub Pages:
Push to GitHub, wait 2 minutes for deployment, then visit:
https://ajaykumarsoma.github.io/Book-Hinduisam/chapters/chapter_01_prana_pratishtha/

---

## 📏 Image Specifications

**Recommended dimensions:**
- **Hero images** (Meenakshi, Tirupati): 1200-1600px width
- **Content images**: 800-1000px width
- **Detail shots** (Ganesha, Lingam): 600-800px width

**File formats:**
- ✅ JPG (best for photos)
- ✅ PNG (best for transparency)
- ✅ WebP (modern, smaller files)

**File size:**
- Keep under 500 KB for fast loading
- Use TinyPNG or ImageOptim to compress

---

## 🎨 Image Quality Tips

1. **High resolution** — At least 800px wide
2. **Good lighting** — Avoid dark/underexposed images
3. **Clean composition** — Subject centered, minimal distractions
4. **Cultural sensitivity** — Respectful depiction of deities/rituals
5. **Attribution** — If using others' photos, credit the photographer

---

**Questions?** Edit this file directly or check the chapter markdown file for placeholder comments.
