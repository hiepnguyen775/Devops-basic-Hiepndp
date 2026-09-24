# 🏗️ projects — Nơi bạn làm dự án

> **Đề bài, yêu cầu và rubric chấm điểm** nằm ở [`../PROJECTS.md`](../PROJECTS.md).
> Thư mục này là **nơi bạn lưu thành quả**.

## Năm dự án

| Thư mục | Dự án | Làm sau | Đề bài |
|---|---|---|---|
| [`project-01-linux-server/`](./project-01-linux-server/) | Máy chủ Linux chuẩn production | Ngày 12 | [PROJECTS.md](../PROJECTS.md#dự-án-01--máy-chủ-linux-chuẩn-production) |
| [`project-02-docker-app/`](./project-02-docker-app/) | Ứng dụng container hoá | Ngày 21 | [PROJECTS.md](../PROJECTS.md#dự-án-02--ứng-dụng-container-hoá) |
| [`project-03-automation/`](./project-03-automation/) | Tự động hoá hạ tầng | Ngày 48 | [PROJECTS.md](../PROJECTS.md#dự-án-03--tự-động-hoá-hạ-tầng) |
| [`project-04-ci-cd/`](./project-04-ci-cd/) | Dây chuyền CI/CD | Ngày 35 | [PROJECTS.md](../PROJECTS.md#dự-án-04--dây-chuyền-cicd) |
| [`project-05-observability/`](./project-05-observability/) | Hệ thống quan sát được | Ngày 51 | [PROJECTS.md](../PROJECTS.md#dự-án-05--hệ-thống-quan-sát-được) |

## Mỗi dự án nên có

```text
project-0X-.../
├── README.md          ← sơ đồ · cách chạy · SỐ LIỆU THẬT · giới hạn
├── src/ hoặc app/
├── infra/             ← Terraform, Ansible, k8s, compose...
├── docs/
│   ├── adr/           ← quyết định lớn + ĐÁNH ĐỔI
│   └── runbook.md
└── TU-CHAM.md         ← điểm tự chấm theo rubric
```

## 💡 Hai lời khuyên quan trọng nhất

**1. Đẩy mỗi dự án lên một repo GitHub riêng.** Nhà tuyển dụng xem GitHub trước khi gọi. Năm repo có README tử tế nói nhiều hơn mọi dòng trong CV.

**2. Ghi số liệu **khi làm**, đừng để cuối mới nhớ.** Thời gian deploy, thời gian rollback, kích thước image, tỉ lệ khả dụng — đó là thứ khiến bạn khác biệt lúc phỏng vấn.

---

[⬅️ README chính](../README.md) · [📋 Đề bài đầy đủ](../PROJECTS.md)
