# OSINT Pipeline

> Automated data collection pipeline for gathering Open Source Intelligence from multiple social media platforms.

## 📋 Overview

This project demonstrates an automated OSINT (Open Source Intelligence) pipeline that collects, processes, and stores publicly available data from social media platforms including Reddit, GitHub, and Instagram.

## 🚀 Features

- **Multi-platform data collection** from Reddit and GitHub APIs
- **Language filtering** to collect English content only
- **Data normalization** across different platform formats
- **Error handling** with graceful degradation
- **Modular architecture** for easy platform integration

## 🛠️ Technologies

- **Python 3.13.7**
- **PRAW** - Reddit API wrapper
- **PyGithub** - GitHub API integration
- **langdetect** - Language detection
- **Virtual environment** for dependency isolation

## 📦 Installation

```bash
# Clone the repository
git clone <repository-url>
cd osint_pipeline

# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
# Reddit API Credentials
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent

# GitHub API Token (optional, increases rate limits)
GITHUB_TOKEN=your_github_token
```

## 🎯 Usage

Run the main pipeline:

```bash
python main.py
```

The pipeline will:
1. Collect data from Reddit (✅)
2. Collect data from GitHub (✅)
3. Attempt Instagram collection (❌ fails due to API restrictions)
4. Filter for English content
5. Store normalized data

## 📂 Project Structure

```
osint_pipeline/
├── main.py              # Main execution script
├── utils/
│   └── cleaner.py       # Data filtering and cleaning
├── config/              # Configuration files
├── data/                # Collected data storage
├── myenv/               # Virtual environment
└── requirements.txt     # Python dependencies
```

## ⚠️ Known Limitations

### Instagram Collection Failed
- **Instaloader library is no longer functional** due to Instagram's GraphQL API restrictions
- Instagram actively blocks automated scraping attempts
- Returns `403 Forbidden` and `401 Unauthorized` errors
- **Success rate: 0%**

### Recommendations:
- Use official Instagram API (requires app approval)
- Focus on Reddit and GitHub for reliable data collection
- Consider alternative platforms (Twitter, Telegram)

## 📊 Sample Results

**Successful Collections:**
- Reddit: 10 records from subreddits
- GitHub: 11 records from repositories
- **Total: 21 records collected**

**Failed Collections:**
- Instagram: 0 records (API deprecated)

## 🔧 Troubleshooting

**Language Detection Errors:**
```python
langdetect.lang_detect_exception.LangDetectException: No features in text.
```
- Caused by empty text fields
- Handled gracefully with try-except blocks

**API Rate Limits:**
- Reddit: 60 requests/min (unauthenticated)
- GitHub: 60 requests/hour (unauthenticated), 5000/hour (authenticated)

## 🎓 Educational Purpose

This project was created for academic purposes to demonstrate:
- API integration and data collection
- ETL (Extract, Transform, Load) processes
- Error handling in data pipelines
- Ethical OSINT practices

## 📝 License

This project is for educational purposes only. Always respect platform Terms of Service and privacy policies when collecting data.

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## ⚡ Future Improvements

- [ ] Add PostgreSQL database integration
- [ ] Implement data visualization dashboard
- [ ] Add more platforms (Twitter, Telegram)
- [ ] Sentiment analysis on collected text
- [ ] Export to CSV/JSON formats
- [ ] Scheduled data collection

---

**Author**: Chris Lopes