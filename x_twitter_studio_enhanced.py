from pathlib import Path
import sqlite3, sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QFrame, QTableWidget, QTableWidgetItem, QHeaderView,
    QMessageBox, QComboBox, QDialog, QFormLayout, QDialogButtonBox,
    QStackedWidget, QAbstractItemView
)

APP_DIR = Path.home() / ".jass_x_studio"
DB_PATH = APP_DIR / "x_studio.db"
ACCOUNTS = [('OpenAI', 'OpenAI', 'AI Labs'), ('OpenAI Developers', 'OpenAIDevs', 'Developer / API'), ('Anthropic', 'AnthropicAI', 'AI Labs'), ('Google DeepMind', 'GoogleDeepMind', 'AI Labs'), ('Google AI', 'GoogleAI', 'AI Labs'), ('AI at Meta', 'AIatMeta', 'AI Labs'), ('Mistral AI', 'MistralAI', 'AI Labs'), ('xAI', 'xai', 'AI Labs'), ('Hugging Face', 'huggingface', 'Open Source AI'), ('NVIDIA AI', 'NVIDIAAI', 'AI Hardware'), ('Microsoft AI', 'MicrosoftAI', 'AI Labs'), ('Cohere', 'CohereAI', 'AI Labs'), ('Perplexity', 'perplexity_ai', 'AI Search'), ('LangChain', 'LangChainAI', 'AI Frameworks'), ('LlamaIndex', 'llama_index', 'AI Frameworks'), ('Replicate', 'replicate', 'AI Platform'), ('Ollama', 'ollama', 'Local AI'), ('LM Studio', 'LMStudioAI', 'Local AI'), ('Runway', 'runwayml', 'AI Video'), ('Midjourney', 'midjourney', 'AI Image'), ('Stability AI', 'StabilityAI', 'AI Image'), ('ElevenLabs', 'elevenlabsio', 'AI Audio'), ('Suno', 'suno_ai_', 'AI Music'), ('Cursor', 'cursor_ai', 'Developer Tools'), ('Replit', 'Replit', 'Developer Tools'), ('Windsurf', 'Windsurf_ai', 'Developer Tools'), ('GitHub', 'github', 'Open Source'), ('GitHub Next', 'githubnext', 'Open Source'), ('JetBrains', 'jetbrains', 'Developer Tools'), ('Vercel', 'vercel', 'Web Development'), ('Cloudflare', 'Cloudflare', 'Cloud / Web'), ('Docker', 'docker', 'Developer Tools'), ('Kubernetes', 'kubernetesio', 'Cloud / DevOps'), ('AWS', 'awscloud', 'Cloud'), ('Google Cloud', 'googlecloud', 'Cloud'), ('Microsoft Azure', 'Azure', 'Cloud'), ('Meta AI Research', 'MetaAI', 'AI Research'), ('BAIR', 'berkeley_ai', 'AI Research'), ('Stanford AI Lab', 'StanfordAILab', 'AI Research'), ('Stanford HAI', 'StanfordHAI', 'AI Research'), ('MIT CSAIL', 'MIT_CSAIL', 'AI Research'), ('Allen AI', 'allen_ai', 'AI Research'), ('Allen Institute for AI', 'allenai', 'AI Research'), ('Mila', 'Mila_Quebec', 'AI Research'), ('FAIR', 'FAIR_Data', 'AI Research'), ('DeepMind', 'DeepMind', 'AI Research'), ('Google Research', 'GoogleResearch', 'AI Research'), ('Microsoft Research', 'MSFTResearch', 'AI Research'), ('Andrej Karpathy', 'karpathy', 'AI Educators'), ('Andrew Ng', 'AndrewYNg', 'AI Educators'), ('Yann LeCun', 'ylecun', 'AI Researchers'), ('François Chollet', 'fchollet', 'AI Researchers'), ('Geoffrey Hinton', 'GeoffreyHinton', 'AI Researchers'), ('Jeff Dean', 'JeffDean', 'AI Researchers'), ('Jim Fan', 'DrJimFan', 'AI Researchers'), ('Simon Willison', 'simonw', 'AI Developers'), ('Sebastian Raschka', 'rasbt', 'AI Educators'), ('Chip Huyen', 'chipro', 'AI Educators'), ('Ethan Mollick', 'emollick', 'AI Educators'), ('Jeremy Howard', 'jeremyphoward', 'AI Educators'), ('François Fleuret', 'fleuret', 'AI Researchers'), ('Lilian Weng', 'lilianweng', 'AI Researchers'), ('Jason Wei', '_jasonwei', 'AI Researchers'), ('Noam Brown', 'polynoamial', 'AI Researchers'), ('Dario Amodei', 'DarioAmodei', 'AI Leaders'), ('Sam Altman', 'sama', 'AI Leaders'), ('Demis Hassabis', 'demishassabis', 'AI Leaders'), ('Aravind Srinivas', 'AravSrinivas', 'AI Leaders'), ('Arthur Mensch', 'arthurmensch', 'AI Leaders'), ('Aidan Gomez', 'aidangomez', 'AI Leaders'), ('Jensen Huang', 'JensenHuang', 'AI Leaders'), ('Satya Nadella', 'satyanadella', 'Tech Leaders'), ('Sundar Pichai', 'sundarpichai', 'Tech Leaders'), ('Elon Musk', 'elonmusk', 'Tech Leaders'), ('Lex Fridman', 'lexfridman', 'AI / Podcasts'), ('Gary Marcus', 'GaryMarcus', 'AI Commentary'), ('Emily Bender', 'emilymbender', 'AI Commentary'), ('François Caron', 'fcaron', 'AI Research'), ('AK', '_akhaliq', 'AI News'), ('AI Pub', 'ai__pub', 'AI News'), ('The AI Scientist', 'AI_Scientist', 'AI Research'), ('Weights & Biases', 'weights_biases', 'ML Tools'), ('MLflow', 'mlflow', 'ML Tools'), ('PyTorch', 'PyTorch', 'ML Frameworks'), ('TensorFlow', 'tensorflow', 'ML Frameworks'), ('Keras', 'keras_io', 'ML Frameworks'), ('scikit-learn', 'scikit_learn', 'ML Frameworks'), ('fast.ai', 'fastdotai', 'AI Education'), ('Gradio', 'GradioML', 'AI Tools'), ('Streamlit', 'streamlit', 'AI Tools'), ('Modal', 'modal_labs', 'AI Infrastructure'), ('Together AI', 'togethercompute', 'AI Infrastructure'), ('Groq', 'GroqInc', 'AI Hardware'), ('AMD', 'AMD', 'AI Hardware'), ('Intel', 'intel', 'AI Hardware'), ('Qualcomm', 'Qualcomm', 'AI Hardware'), ('Scale AI', 'scale_ai', 'AI Data'), ('Databricks', 'databricks', 'Data / AI'), ('Snowflake', 'Snowflake', 'Data / AI'), ('Mozilla', 'mozilla', 'Open Source / Web')]

STYLE = """
QMainWindow, QWidget { background:#0b1220; color:#e5e7eb; font-family:"Segoe UI"; }
QFrame#sidebar { background:#0f172a; border-right:1px solid #263449; }
QLabel#brand { color:#f8fafc; font-size:22px; font-weight:800; }
QLabel#brandSub { color:#64748b; font-size:10px; font-weight:700; letter-spacing:2px; }
QLabel#pageTitle { color:#f8fafc; font-size:26px; font-weight:800; }
QLabel#muted { color:#94a3b8; }
QLabel#statValue { color:#f8fafc; font-size:24px; font-weight:800; }
QLabel#statLabel { color:#94a3b8; font-size:11px; }
QPushButton#nav {
    text-align:left; padding:12px 15px; border:0; border-radius:9px;
    color:#94a3b8; background:transparent; font-size:14px;
}
QPushButton#nav:hover { background:#172238; color:#f8fafc; }
QPushButton#nav:checked { background:#1d4ed8; color:white; font-weight:700; }
QLineEdit, QComboBox {
    background:#111c2f; border:1px solid #2b3a52; border-radius:9px;
    padding:10px 12px; color:#f8fafc; min-height:20px;
}
QLineEdit:focus { border:1px solid #3b82f6; }
QPushButton#primary {
    background:#2563eb; color:white; border:0; border-radius:9px;
    padding:10px 16px; font-weight:700;
}
QPushButton#primary:hover { background:#3b82f6; }
QPushButton#secondary {
    background:#172238; color:#cbd5e1; border:1px solid #2b3a52;
    border-radius:9px; padding:9px 14px;
}
QPushButton#secondary:hover { background:#22314b; color:white; }
QFrame#stat {
    background:#111c2f; border:1px solid #26364e; border-radius:13px;
}
QFrame#card {
    background:#111c2f; border:1px solid #26364e; border-radius:13px;
}
QFrame#card:hover { border:1px solid #3b82f6; background:#14223a; }
QTableWidget {
    background:#0f192a; border:1px solid #26364e; border-radius:10px;
    gridline-color:#1f2d42; alternate-background-color:#111c2f;
}
QHeaderView::section {
    background:#162238; color:#94a3b8; padding:9px; border:0;
    font-weight:700;
}
QListWidget { background:transparent; border:0; }
QListWidget::item { padding:10px; border-radius:8px; }
QListWidget::item:selected { background:#1d4ed8; color:white; }
"""

class DB:
    def __init__(self):
        APP_DIR.mkdir(parents=True, exist_ok=True)
        self.c = sqlite3.connect(DB_PATH)
        self.c.row_factory = sqlite3.Row
        self.c.execute("""CREATE TABLE IF NOT EXISTS accounts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, handle TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL, favorite INTEGER DEFAULT 0,
            notes TEXT DEFAULT '')""")
        for n,h,cat in ACCOUNTS:
            self.c.execute("INSERT OR IGNORE INTO accounts(name,handle,category) VALUES(?,?,?)",(n,h,cat))
        self.c.commit()

    def all(self, q="", fav=False, cat="All Categories"):
        sql="SELECT * FROM accounts WHERE 1=1"; args=[]
        if fav: sql+=" AND favorite=1"
        if cat != "All Categories": sql+=" AND category=?"; args.append(cat)
        if q:
            sql+=" AND (name LIKE ? OR handle LIKE ? OR category LIKE ?)"
            x=f"%{q}%"; args += [x,x,x]
        return self.c.execute(sql+" ORDER BY category,name",args).fetchall()

class AddDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent); self.setWindowTitle("Add X / Twitter Page")
        self.setMinimumWidth(420); f=QFormLayout(self)
        self.name=QLineEdit(); self.handle=QLineEdit(); self.category=QLineEdit("My Pages")
        self.name.setPlaceholderText("e.g. My favorite AI researcher")
        self.handle.setPlaceholderText("@username")
        f.addRow("Page name",self.name); f.addRow("Handle",self.handle); f.addRow("Category",self.category)
        b=QDialogButtonBox(QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Cancel)
        b.accepted.connect(self.accept); b.rejected.connect(self.reject); f.addWidget(b)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(); self.db=DB(); self.setWindowTitle("JASS X / TWITTER STUDIO")
        self.resize(1280,800); self.setMinimumSize(1050,680); self.build(); self.refresh()

    def build(self):
        root=QWidget(); self.setCentralWidget(root); main=QHBoxLayout(root); main.setContentsMargins(0,0,0,0); main.setSpacing(0)

        side=QFrame(); side.setObjectName("sidebar"); side.setFixedWidth(225); sl=QVBoxLayout(side); sl.setContentsMargins(16,22,16,16)
        brand=QLabel("JASS X / TWITTER STUDIO"); brand.setObjectName("brand"); brand.setWordWrap(True); sl.addWidget(brand)
        sub=QLabel("CURATED SOCIAL HUB"); sub.setObjectName("brandSub"); sl.addWidget(sub); sl.addSpacing(25)

        self.nav=[]
        for label in ["⌂  Dashboard","◉  All Pages","★  Favorites","▦  Categories"]:
            b=QPushButton(label); b.setObjectName("nav"); b.setCheckable(True); b.clicked.connect(lambda _,x=len(self.nav):self.goto(x)); self.nav.append(b); sl.addWidget(b)
        sl.addStretch()
        info=QLabel("100 curated pages\nAI • Tech • Research\nOpen Source • Developers")
        info.setObjectName("muted"); info.setWordWrap(True); sl.addWidget(info)
        main.addWidget(side)

        content=QWidget(); cl=QVBoxLayout(content); cl.setContentsMargins(28,25,28,25); cl.setSpacing(18); main.addWidget(content,1)

        head=QHBoxLayout()
        self.title=QLabel("Dashboard"); self.title.setObjectName("pageTitle"); head.addWidget(self.title)
        head.addStretch()
        self.search=QLineEdit(); self.search.setFixedWidth(300); self.search.setPlaceholderText("⌕  Search pages...")
        self.search.textChanged.connect(self.refresh); head.addWidget(self.search)
        add=QPushButton("＋ Add Page"); add.setObjectName("primary"); add.clicked.connect(self.add_page); head.addWidget(add)
        cl.addLayout(head)

        self.stack=QStackedWidget(); cl.addWidget(self.stack,1)
        self.make_dashboard(); self.make_pages(); self.make_categories()
        self.goto(0)

    def stat(self,label,value):
        f=QFrame(); f.setObjectName("stat"); l=QVBoxLayout(f); l.setContentsMargins(16,13,16,13)
        v=QLabel(str(value)); v.setObjectName("statValue"); t=QLabel(label); t.setObjectName("statLabel"); l.addWidget(v); l.addWidget(t); return f

    def make_dashboard(self):
        w=QWidget(); l=QVBoxLayout(w); l.setSpacing(18)
        self.stats=QHBoxLayout()
        for i in range(4): self.stats.addWidget(QFrame())
        l.addLayout(self.stats)
        intro=QFrame(); intro.setObjectName("card"); il=QVBoxLayout(intro)
        a=QLabel("Your AI & Technology Feed"); a.setFont(QFont("Segoe UI",18,QFont.Weight.Bold))
        il.addWidget(a); b=QLabel("A local launchpad for 100 useful X pages. Double-click any row or use Open on X.")
        b.setObjectName("muted"); il.addWidget(b); l.addWidget(intro)
        self.recent=QTableWidget(0,4); self.recent.setHorizontalHeaderLabels(["Page","Handle","Category","Action"])
        self.recent.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.recent.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers); self.recent.doubleClicked.connect(self.open_recent)
        l.addWidget(self.recent,1); self.stack.addWidget(w)

    def make_pages(self):
        w=QWidget(); l=QVBoxLayout(w); l.setSpacing(12)
        bar=QHBoxLayout(); self.cat=QComboBox(); self.cat.addItem("All Categories")
        self.cat.currentIndexChanged.connect(self.refresh); bar.addWidget(self.cat); bar.addStretch()
        self.count=QLabel(); self.count.setObjectName("muted"); bar.addWidget(self.count); l.addLayout(bar)
        self.table=QTableWidget(0,5); self.table.setHorizontalHeaderLabels(["Page","Handle","Category","★","Open"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers); self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.doubleClicked.connect(self.open_table); l.addWidget(self.table,1); self.stack.addWidget(w)

    def make_categories(self):
        w=QWidget(); l=QVBoxLayout(w); title=QLabel("Explore by Category"); title.setFont(QFont("Segoe UI",18,QFont.Weight.Bold)); l.addWidget(title)
        self.catlist=QListWidget(); self.catlist.itemDoubleClicked.connect(lambda i:self.search_category(i.data(Qt.ItemDataRole.UserRole))); l.addWidget(self.catlist); self.stack.addWidget(w)

    def goto(self,n):
        for i,b in enumerate(self.nav): b.setChecked(i==n)
        self.stack.setCurrentIndex(0 if n==0 else 1 if n in (1,2) else 2)
        self.title.setText(["Dashboard","All Pages","Favorites","Categories"][n])
        if n==2: self.filter_favorites=True
        else: self.filter_favorites=False
        self.refresh()

    def refresh(self):
        if not hasattr(self,"table"): return
        # Update category selector once.
        cats=[r["category"] for r in self.db.c.execute("SELECT DISTINCT category FROM accounts ORDER BY category")]
        current=self.cat.currentText() if self.cat.count() else "All Categories"
        self.cat.blockSignals(True); self.cat.clear(); self.cat.addItem("All Categories"); self.cat.addItems(cats)
        self.cat.setCurrentText(current if current in cats else "All Categories"); self.cat.blockSignals(False)

        rows=self.db.all(self.search.text().strip(), getattr(self,"filter_favorites",False), self.cat.currentText())
        self.table.setRowCount(len(rows))
        for r,row in enumerate(rows):
            self.table.setItem(r,0,QTableWidgetItem(row["name"])); self.table.setItem(r,1,QTableWidgetItem("@"+row["handle"]))
            self.table.setItem(r,2,QTableWidgetItem(row["category"]))
            fav=QTableWidgetItem("★" if row["favorite"] else "☆"); fav.setTextAlignment(Qt.AlignmentFlag.AlignCenter); self.table.setItem(r,3,fav)
            btn=QPushButton("Open ↗"); btn.setObjectName("secondary"); btn.clicked.connect(lambda _,h=row["handle"]:self.open_handle(h)); self.table.setCellWidget(r,4,btn)
            self.table.item(r,0).setData(Qt.ItemDataRole.UserRole,row["id"])
        self.count.setText(f"{len(rows)} pages")
        self.refresh_dashboard()
        self.refresh_categories()

    def refresh_dashboard(self):
        if not hasattr(self,"recent"): return
        rows=self.db.all()[:12]
        self.recent.setRowCount(len(rows))
        for r,row in enumerate(rows):
            self.recent.setItem(r,0,QTableWidgetItem(row["name"])); self.recent.setItem(r,1,QTableWidgetItem("@"+row["handle"]))
            self.recent.setItem(r,2,QTableWidgetItem(row["category"]))
            b=QPushButton("Open ↗"); b.setObjectName("secondary"); b.clicked.connect(lambda _,h=row["handle"]:self.open_handle(h)); self.recent.setCellWidget(r,3,b)
            self.recent.item(r,0).setData(Qt.ItemDataRole.UserRole,row["id"])
        total=self.db.c.execute("SELECT COUNT(*) FROM accounts").fetchone()[0]
        fav=self.db.c.execute("SELECT COUNT(*) FROM accounts WHERE favorite=1").fetchone()[0]
        cats=self.db.c.execute("SELECT COUNT(DISTINCT category) FROM accounts").fetchone()[0]
        for i,(lab,val) in enumerate([("Total Pages",total),("Favorites",fav),("Categories",cats),("Curated",100)]):
            old=self.stats.itemAt(i).widget()
            self.stats.replaceWidget(old,self.stat(lab,val)); old.deleteLater()

    def refresh_categories(self):
        if not hasattr(self,"catlist"): return
        rows=self.db.c.execute("SELECT category,COUNT(*) n FROM accounts GROUP BY category ORDER BY category").fetchall()
        self.catlist.clear()
        for row in rows:
            item=QListWidgetItem(f"▦  {row['category']}    ·    {row['n']} pages    ·    double-click to filter")
            item.setData(Qt.ItemDataRole.UserRole,row["category"]); self.catlist.addItem(item)

    def search_category(self,cat):
        self.goto(1); self.cat.setCurrentText(cat); self.search.setText("")

    def open_handle(self,h): QDesktopServices.openUrl(QUrl("https://x.com/"+h))
    def open_table(self,i): 
        item=self.table.item(i.row(),0)
        if item:
            row=self.db.c.execute("SELECT handle FROM accounts WHERE id=?",(item.data(Qt.ItemDataRole.UserRole),)).fetchone()
            if row: self.open_handle(row["handle"])
    def open_recent(self,i):
        item=self.recent.item(i.row(),0)
        if item:
            row=self.db.c.execute("SELECT handle FROM accounts WHERE id=?",(item.data(Qt.ItemDataRole.UserRole),)).fetchone()
            if row: self.open_handle(row["handle"])

    def add_page(self):
        d=AddDialog(self)
        if d.exec()!=QDialog.DialogCode.Accepted: return
        n=d.name.text().strip(); h=d.handle.text().strip().lstrip("@").replace("https://x.com/","").strip("/"); c=d.category.text().strip() or "My Pages"
        if not n or not h: QMessageBox.warning(self,"Missing information","Name and handle are required."); return
        try:
            self.db.c.execute("INSERT INTO accounts(name,handle,category) VALUES(?,?,?)",(n,h,c)); self.db.c.commit(); self.refresh()
        except sqlite3.IntegrityError: QMessageBox.warning(self,"Already exists","That X handle is already in the Studio.")

def main():
    app=QApplication(sys.argv); app.setStyle("Fusion"); app.setStyleSheet(STYLE)
    w=MainWindow(); w.show(); sys.exit(app.exec())
if __name__=="__main__": main()
