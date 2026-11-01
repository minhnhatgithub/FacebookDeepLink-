# 🚀 Facebook Katana Deeplink Master Database

<p align="center">
  <img src="https://img.shields.io/badge/Total%20Deeplinks-1172-blue?style=for-the-badge&logo=facebook" alt="Total Deeplinks"/>
  <img src="https://img.shields.io/badge/Schemes-fb%20%7C%20fbinternal%20%7C%20dialtone%20%7C%20fbrpc-green?style=for-the-badge" alt="Schemes"/>
  <img src="https://img.shields.io/badge/App-Facebook%20Katana-0866FF?style=for-the-badge&logo=meta" alt="Facebook Katana"/>
</p>

Comprehensive, authenticated dataset of **1172 Deeplinks** extracted directly from **Facebook Katana ART Execution Bytecode (158MB `z-*.vdex`)** on Android.

---

## 📌 Tổng Quan Bộ Dữ Liệu (Overview)

Facebook Katana (ứng dụng Facebook chính thức trên Android) sử dụng cổng điều hướng `com.facebook.katana.IntentUriHandler` để đón bắt các URL scheme tùy biến và điều hướng sâu vào các màn hình ngầm mà không cần đi qua thanh điều hướng thông thường.

Dữ liệu này được trích xuất trực tiếp từ bộ nhớ bytecode đã biên dịch của ứng dụng, bao gồm cả các endpoint công khai lẫn các URI nội bộ dành riêng cho lập trình viên Meta.

### Thống Kê Các Scheme (Schemes Breakdown):
- **`fb://`**: 869 Endpoints (Trang cá nhân, Reels, Watch, Marketplace, Groups, Fanpage, Checkpoint...)
- **`fbinternal://`**: 295 Endpoints (Cài đặt nội bộ, OTA, debug viễn thông, tính năng thử nghiệm Meta)
- **`dialtone://`**: 4 Endpoints (Chế độ sử dụng mạng không tốn dung lượng Free Basics)
- **`fbrpc://`**: 4 Endpoints (Giao thức Remote Procedure Call nội bộ Meta)

---

## 📂 Danh Mục Phân Loại (Categories)

| Danh Mục (Category) | Số Lượng URI | Mô Tả |
|---|---|---|
| **Internal & Developer Utilities (Nội Bộ Meta & Viễn Thông)** | `383` | Các liên kết điều hướng chuyên biệt |
| **Profile & Social Graph (Trang Cá Nhân & Bạn Bè)** | `156` | Các liên kết điều hướng chuyên biệt |
| **Reels, Watch, Video & Media** | `148` | Các liên kết điều hướng chuyên biệt |
| **Feed & Composer (Bảng Tin & Soạn Bài Viết)** | `126` | Các liên kết điều hướng chuyên biệt |
| **Settings & Privacy (Cài Đặt & Quyền Riêng Tư)** | `70` | Các liên kết điều hướng chuyên biệt |
| **Messaging & Broadcast Channels (Tin Nhắn & Kênh)** | `62` | Các liên kết điều hướng chuyên biệt |
| **Groups & Communities (Hội Nhóm)** | `61` | Các liên kết điều hướng chuyên biệt |
| **Marketplace, Shopping & Meta Pay** | `61` | Các liên kết điều hướng chuyên biệt |
| **Account & Authentication (Bảo Mật & Checkpoint)** | `46` | Các liên kết điều hướng chuyên biệt |
| **Pages & Business (Fanpage & Doanh Nghiệp)** | `43` | Các liên kết điều hướng chuyên biệt |
| **Generative AI & Meta Bots** | `16` | Các liên kết điều hướng chuyên biệt |

---

## ⚡ Các Deeplink Nổi Bật (High-Value Highlights)

### 1. Bảo Mật, Khôi Phục & Checkpoint (Security & Recovery)
* `fb://checkpoint_epsilon/` - Nhảy thẳng vào màn hình xử lý Checkpoint tài khoản.
* `fb://approve_from_another_device/open` - Màn hình phê duyệt đăng nhập từ thiết bị khác.
* `fb://account/recovery` - Cổng khôi phục tài khoản khẩn cấp.
* `fb://otp?id={username}&pass={otp}` - Tự động điền OTP đăng nhập.
* `fb://hacked/disavow` - Gỡ quyền truy cập khi tài khoản bị hack.
* `fb://two_step_verification` - Cài đặt xác thực 2 yếu tố (2FA).

### 2. Tự Động Hóa & Tương Tác (Automation / Farm / Bot)
* `fb://feed` - Mở trực tiếp Bảng tin (News Feed).
* `fb://fb_shorts/viewer` - Trình lướt video ngắn Reels toàn màn hình.
* `fb://reel/{reel_id}` - Mở thẳng 1 video Reel cụ thể.
* `fb://watch` - Tab video Facebook Watch.
* `fb://live` - Danh sách livestream đang phát sóng.
* `fb://allactivity` - Xem toàn bộ nhật ký hoạt động cá nhân.

### 3. Marketplace & Mua Sắm (Commerce)
* `fb://marketplace` - Mở chợ Marketplace.
* `fb://marketplace_search?query={keyword}` - Tìm kiếm trực tiếp sản phẩm.
* `fb://marketplace_product_details?listing_id={id}` - Chi tiết bài đăng bán hàng.
* `fb://facebook_pay` - Mở ví thanh toán Meta Pay.

### 4. Cài Đặt Hệ Thống & Giao Diện (Settings)
* `fb://dark_mode_settings/?entry=search` - Bật/tắt Dark Mode tức thì.
* `fb://tab_hiding_settings/` - Cài đặt ẩn các tab trên thanh điều hướng Facebook.
* `fb://notification_settings_email` - Tùy chỉnh thông báo gửi về Email.

### 5. Meta AI & Tính Năng Độc Quyền (Generative AI)
* `fb://gen_ai_chat/?as_bottom_sheet=1` - Cửa sổ chat bot Meta AI dạng bottom sheet.
* `fb://ai_manage_memory` - Quản lý bộ nhớ AI đã lưu về người dùng.
* `fb://video_gen_ai_create?id={id}` - Trình tạo video AI của Meta.

---

## 🛠️ Hướng Dẫn Sử Dụng (Usage Guide)

### 1. Sử Dụng Trực Tiếp Qua Lệnh ADB (Android Debug Bridge):
```bash
adb shell am start -a android.intent.action.VIEW -d "<URI>"
```
*Ví dụ:*
```bash
# Mở thẳng giao diện Marketplace
adb shell am start -a android.intent.action.VIEW -d "fb://marketplace"

# Mở thẳng trình xem Reels
adb shell am start -a android.intent.action.VIEW -d "fb://fb_shorts/viewer"

# Mở trình giải Checkpoint
adb shell am start -a android.intent.action.VIEW -d "fb://checkpoint_epsilon/"
```

### 2. Sử Dụng Tool Python Có Sẵn Trong Repo:
```bash
python deeplink_caller.py "fb://marketplace"
# Hoặc chỉ định serial thiết bị:
python deeplink_caller.py "fb://feed" -s 5200e93dee335407
```

### 3. Gọi Từ Mã Nguồn Ứng Dụng Android (Java / Kotlin):
```java
Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("fb://marketplace"));
intent.setPackage("com.facebook.katana");
context.startActivity(intent);
```

---

## 📦 Định Dạng Tệp Tin Có Sẵn Trong Kho (Repository Structure):
* **`README.md`**: Tài liệu hướng dẫn và danh mục tổng quan.
* **`facebook_deeplinks.json`**: File JSON cấu trúc đầy đủ 1.172 endpoints để tích hợp vào tool/code.
* **`facebook_deeplinks.csv`**: File bảng tính CSV dễ dàng xem trên Microsoft Excel hoặc Google Sheets.
* **`facebook_deeplinks_raw.txt`**: Danh sách thô toàn bộ liên kết (mỗi liên kết 1 dòng).
* **`deeplink_caller.py`**: Công cụ dòng lệnh hỗ trợ test nhanh trên Android qua ADB.

---

<p align="center">
  <b>Bản quyền &amp; Phát triển bởi <a href="https://github.com/minhnhatgithub">minhnhatgithub</a></b>
</p>
