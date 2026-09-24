# 🎓 capstone — Dự án tốt nghiệp

> **Đề bài đầy đủ:** [Ngày 56–59](../Giai-doan-4-SRE-Capstone.md#ngày-56--dự-án-tốt-nghiệp--phần-1-thiết-kế--hạ-tầng) · **Bộ khung code sẵn:** [`../capstone-cloudnote/`](../capstone-cloudnote/)

Đây là nơi bạn xây **hệ thống của riêng mình** — không phải bản sao của bộ khung.

## Bốn phần

| Phần | Nội dung | Điểm | Đề bài |
|---|---|---|---|
| 1 | Thiết kế & Hạ tầng | 25 | [Ngày 56](../Giai-doan-4-SRE-Capstone.md#ngày-56--dự-án-tốt-nghiệp--phần-1-thiết-kế--hạ-tầng) |
| 2 | Container & CI/CD | 30 | [Ngày 57](../Giai-doan-4-SRE-Capstone.md#ngày-57--dự-án-tốt-nghiệp--phần-2-container--cicd) |
| 3 | Giám sát & Độ tin cậy | 30 | [Ngày 58](../Giai-doan-4-SRE-Capstone.md#ngày-58--dự-án-tốt-nghiệp--phần-3-monitoring--reliability) |
| 4 | Tài liệu & Portfolio | 15 | [Ngày 59](../Giai-doan-4-SRE-Capstone.md#ngày-59--dự-án-tốt-nghiệp--phần-4-tài-liệu-demo--portfolio) |

**Đạt 80/100 trở lên** là một dự án portfolio mạnh.

## Cấu trúc đề xuất

```text
capstone/
├── README.md              ← sơ đồ · cách chạy · số liệu · GIỚI HẠN
├── app/{backend,frontend}/
├── terraform/{modules,envs}/
├── helm/
├── .github/workflows/
└── docs/
    ├── kien-truc.md
    ├── adr/               ← ít nhất 3 ADR có mục ĐÁNH ĐỔI
    ├── runbook.md         ← ít nhất 3 sự cố
    └── dien-tap.md        ← kết quả 6 kịch bản phá hệ thống
```

## Tiến độ

- [ ] Phần 1 — Thiết kế & Hạ tầng · ___/25
- [ ] Phần 2 — Container & CI/CD · ___/30
- [ ] Phần 3 — Giám sát & Độ tin cậy · ___/30
- [ ] Phần 4 — Tài liệu & Portfolio · ___/15
- [ ] **Tổng: ___/100**

## Số liệu thật (điền khi làm)

| Chỉ số | Giá trị |
|---|---|
| Thời gian từ commit tới chạy thật | |
| Thời gian rollback | |
| Khả dụng (7 ngày) | |
| RTO khôi phục database | |
| Kích thước image | |

> 💡 **Hai mục gây ấn tượng nhất mà hiếm ai làm:** *"Số liệu thật"* và *"Giới hạn hiện tại"*. Con số cho thấy bạn **đo** chứ không đoán; nêu giới hạn cho thấy bạn **hiểu** hệ thống của mình.

---

[⬅️ README chính](../README.md) · [🏗️ PROJECTS](../PROJECTS.md)
