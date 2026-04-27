# 🚀 Quick Instructions: Add Images to Chapter 1

## What You Need to Do

You need to replace **5 placeholder URLs** with actual image URLs in the chapter file.

---

## Step 1: Get Images

Choose ONE method:

### Option A: Generate with AI (Recommended)
1. Use ChatGPT DALL-E, Midjourney, or Stable Diffusion
2. **Copy prompts from** `IMAGE_GUIDE.md` (see "AI Generation Prompt" for each image)
3. Generate 5 images
4. Download them

### Option B: Search & Download
1. Use search strings from `IMAGE_GUIDE.md`
2. Search on Google Images, Wikimedia Commons, Unsplash, or Pexels
3. Download 5 high-quality images (800px+ width)

### Option C: Take Your Own Photos
1. Visit local Hindu temples
2. Photograph with permission
3. Use high resolution (800px+ width)

---

## Step 2: Upload Images to Imgur

**For each of the 5 images:**

1. Go to: https://imgur.com/upload
2. Drag and drop your image
3. After upload, **right-click the image** → **Copy image address**
4. Save the URL (will look like: `https://i.imgur.com/ABC123.jpg`)

---

## Step 3: Edit the Chapter File

1. Open: `docs/chapters/chapter_01_prana_pratishtha.md`
2. Find: `IMAGE_URL_1` (it's on line ~12)
3. Replace with your Imgur URL:
   ```markdown
   ![Meenakshi Temple](https://i.imgur.com/YOUR_URL_HERE.jpg)
   ```
4. Repeat for `IMAGE_URL_2`, `IMAGE_URL_3`, `IMAGE_URL_4`, `IMAGE_URL_5`

### Quick Find & Replace:

| Placeholder | Line # (approx) | Image Description |
|-------------|-----------------|-------------------|
| `IMAGE_URL_1` | 12 | Meenakshi Temple |
| `IMAGE_URL_2` | 28 | Fire Ritual (Homa) |
| `IMAGE_URL_3` | 498 | Ganesha Murti |
| `IMAGE_URL_4` | 863 | Shiva Lingam |
| `IMAGE_URL_5` | 1196 | Tirupati Temple |

---

## Step 4: Save & Deploy

### Commit changes:
```bash
cd Book-Hinduisam
git add docs/chapters/chapter_01_prana_pratishtha.md
git commit -m "Add images to Chapter 1"
git push origin main
```

### Wait 2 minutes for GitHub Actions to deploy

### View your book:
https://ajaykumarsoma.github.io/Book-Hinduisam/chapters/chapter_01_prana_pratishtha/

---

## 📸 The 5 Images You Need

1. **Meenakshi Temple** — Colorful gopuram tower (Madurai)
2. **Fire Ritual** — Priest performing homa with flames
3. **Ganesha** — Bronze elephant-headed deity statue
4. **Shiva Lingam** — Black stone cylindrical form with water
5. **Tirupati Temple** — Golden gopuram on hills

---

## ⚡ Super Quick Method (Using AI)

If you have ChatGPT Plus or Midjourney:

1. Open `IMAGE_GUIDE.md`
2. Copy the 5 "AI Generation Prompt" sections
3. Generate all 5 images
4. Upload to Imgur
5. Replace IMAGE_URL_1 through IMAGE_URL_5
6. Commit & push
7. **Done in 10 minutes!**

---

**Full details:** See `IMAGE_GUIDE.md` for comprehensive instructions, prompts, and search strings.
