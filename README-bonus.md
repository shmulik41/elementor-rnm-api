# שלב הבונוס – Elementor DevOps Home Exercise

## סקירה
בשלב הבונוס נרחיב את שלב החובה, כך שהאפליקציה תעבוד כשירות אינטרנטי (REST API) ונפרוס אותה בסביבות שונות:
1. Dockerizing as Service
2. Kubernetes Deployment
3. Helm Chart Deployment
4. GitHub Actions Workflow

---

## 1. Dockerizing as Service
### מה נעשה:
- הפיכת הקוד לשירות REST API עם Flask (כבר בוצע).
- יצירת Dockerfile לבניית image.
- הוראות להרצת האפליקציה בתוך Docker.

### הוראות הרצה (מקומית)
```bash
pip install -r requirements.txt
python src/app.py
