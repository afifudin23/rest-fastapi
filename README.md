# Rest API with FastAPI

## Task1 Backend Solvera OJT - Software Developer

## 1. Fokus utama

- Memahami **cara berpikir backend**:
    - Konstruksi alur data
    - Logika bisnis
    - Integrasi dengan database & API

---

## 2. Hal-hal yang dicatat

### Efisiensi

- Gunakan query yang tepat agar **mengurangi jumlah query ke database**.
- Gunakan migration database untuk mempermudah bekerja dalam tim

### Struktur kode

- Pisahkan **models, schemas, routers, services** agar modul mudah dipelihara.
- Gunakan **dependency injection** untuk session/database.

### Modul

- `SQLModel / SQLAlchemy` untuk ORM.
- `FastAPI` untuk endpoint & routing.
- `Pydantic` untuk validasi request/response.
- `PyJWT / Passlib[argon2]` untuk autentikasi & hashing password.

---

## 3. Mini-exercise: Endpoint sederhana

Buat endpoint sederhana di FastAPI dengan konsep berikut:

- User harus **login** (autentikasi JWT) untuk membuat post.
- Semua orang bisa **melihat daftar semua posts** tanpa login.
- Hanya **pemilik post** yang bisa melakukan **edit** atau **delete** post tersebut.
- Gunakan konsep **Pydantic schemas** untuk validasi request dan response, serta **SQLModel** untuk integrasi database.

## 4. Aha moments

- Memisahkan models, schemas, routers, services membuat kode lebih rapi dan mudah diuji.
- Pydantic + orm_mode mempermudah mapping object database ke response JSON.
- Dependency injection (Depends) memungkinkan akses session atau auth secara bersih tanpa hardcode.
- JWT + middleware/dependency membuat route tertentu “terproteksi”.

## 5. Area yang ingin didalami

- Bagaimana struktur folder ideal untuk proyek backend berskala menengah/besar agar mudah dikelola oleh tim?
- Bagaimana caranya supaya kita mampu menyeseuaikan diri dalam bekerja didalam tim (kolaborasi tim)?

## 6. Instalasi

Ikuti langkah-langkah berikut untuk menjalankan project:

```bash
git clone git@github.com:afifudin23/Task1-BE-Afifudin-Nurfalah.git
cd Task1-BE-Afifudin-Nurfalah

python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
cp .env.example .env

# URL koneksi database PostgreSQL
# Format: postgresql+psycopg2://<username>:<password>@<host>:<port>/<database_name>
DATABASE_URL="postgresql+psycopg2://postgres:password@localhost:5432/dbname"
JWT_SECRET="RAHASIA" # Secret key untuk JWT (JSON Web Token)

# DB Migrations
alembic upgrade head

# Jalankan Server
fastapi dev main.py
```
Untuk mempermudah testing API, import file **Task1 Backend Rest - FastAPI.postman_collection.json ke postman.