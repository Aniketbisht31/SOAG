

#  SOAG

AI-powered system that recommends optimal algorithms based on problem descriptions and analyzes their complexity.

---

##  Features

* Algorithm recommendation from natural language input
* Constraint-based selection
* Master Theorem complexity solver
* FastAPI backend with Swagger documentation

---

##  Tech Stack

* Python
* FastAPI
* Pydantic

---

##  Run Project

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints

### 🔍 Recommend Algorithm

`POST /recommend`

Example:

```json
{
  "description": "Search element in sorted array"
}
```

---

###  Master Theorem Solver

`POST /master-theorem`

Example:

```json
{
  "a": 2,
  "b": 2,
  "k": 1
}
```

---

##  Completed

* [x] Problem analyzer
* [x] Algorithm database
* [x] Recommendation engine
* [x] Master theorem solver
* [x] FastAPI backend

---

##  Upcoming Goals

* [ ] AI-based problem understanding
* [ ] Benchmark simulation
* [ ] Code generation for algorithms
* [ ] Web dashboard

---


