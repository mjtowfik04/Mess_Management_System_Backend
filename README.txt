MESS MANAGEMENT SYSTEM
Production by Towfik

---

1. PROJECT OVERVIEW

---

Mess Management System হলো একটি web application যেখানে একটি mess / hostel এর:

* Member management
* Meal tracking
* Deposit tracking
* Bazar cost tracking
* Meal rate calculation
* Balance calculation

সহজে পরিচালনা করা যায়।

Backend: Django + Django Rest Framework
Frontend: React.js + Tailwind / Bootstrap
Database: SQLite / MySQL

---

2. MAIN FEATURES

---

1. User Authentication

* Register
* Login
* JWT Authentication

2. Member Management

* All mess members list
* Member profile
* Role based system (Admin / Member)

3. Meal Management

* Lunch count
* Dinner count
* Guest meal
* Monthly meal tracking

4. Deposit System

* Member deposit add
* Deposit history
* Total deposit calculation

5. Bazar Cost System

* Daily bazar cost
* Extra charge
* Total cost calculation

6. Meal Rate Calculation
   System automatically calculates:

Meal Rate = (Total Bazar Cost + Extra Charge) / Total Meals

7. Member Cost Calculation

Member Meal Cost =
Total Member Meals × Meal Rate

8. Balance Calculation

Balance =
Total Deposit - Meal Cost

---

3. PROJECT STRUCTURE

---

Backend Apps:

Users

* Custom user model
* Authentication

Meals

* Meal entry
* Meal calculation

Billing

* Member deposit system

Bazar

* Meal cost
* Extra charges

---

4. IMPORTANT MODELS

---

User

* id
* email
* first_name
* last_name
* is_staff

Meal

* member
* month
* lunch
* dinner
* is_guest
* date

AddMemberMoney

* member
* deposit_amount
* date

Add_Cost

* meal_cost
* date

Extra_Charge

* extra_charge
* reason

---

5. API FEATURES (DRF)

---

User API
GET /users/

Meal API
GET /meals/
POST /meals/

Deposit API
POST /deposit/

Cost API
POST /add-cost/

---

6. SYSTEM CALCULATIONS

---

Total Meals =
Sum(lunch + dinner + guest)

Meal Rate =
(Total Bazar Cost + Extra Charge) / Total Meals

Member Meal Cost =
Member Total Meals × Meal Rate

Balance =
Total Deposit - Member Meal Cost

---

7. FRONTEND FEATURES

---

React UI Pages:

Dashboard
All Members
Add Meal
Meal History
Deposit History
Bazar Cost
Profile

Extra Features:

* User search
* Auto refresh messages
* Clean UI
* Responsive design

---

8. SECURITY

---

Role Based Access Control (RBAC)

Admin

* Manage members
* Add cost
* View reports

Member

* View meals
* View deposit
* View balance

---

9. FUTURE IMPROVEMENTS

---

* PDF report export
* Monthly report download
* Mobile app
* Notification system
* Auto bazar analytics

---

10. AUTHOR

---

Name: Towfik Islam
Email: [mjtowfik653672@gmail.com](mailto:mjtowfik653672@gmail.com)
Portfolio: https://mjtowfik2004.vercel.app/
LinkedIn: https://www.linkedin.com/in/towfik-islam-79aa262b6

---

