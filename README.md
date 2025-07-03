# Gym-membership-management-system

A secure and modular Python application designed to streamline gym operations by enabling effective management of members, memberships, and activities. Built using Python and SQLite, this system supports both administrator and member access with a clear separation of privileges and strong focus on usability and data privacy.

---

## 🎯 Project Purpose

This system addresses common operational challenges faced by gyms by:

- Ensuring the **right information reaches the right users** (members vs admins)
- Supporting business decision-making through data insights
- Improving **customer satisfaction** by helping members fully understand and utilize their membership packages
- Maintaining **security and data privacy** by restricting access based on roles

---

## 👥 Target Users

| Role      | Key Access and Features                                  |
|-----------|-----------------------------------------------------------|
| Admin     | View/edit members, manage activities, monitor packages    |
| Member    | Sign up, log in securely, view membership, edit package   |

---

## 🧩 Features

- 🔐 **Secure login system** using password hashing (SHA-256)
- 🧾 **Member registration** with package and activity selection
- 🧑‍💼 **Admin dashboard** to view and manage all member and activity data
- 📋 **Package enforcement**: Admins can limit access to facilities based on selected membership
- 📊 **Business insights**: Admins can track member counts to guide business scaling
- 🧱 **Modular and extensible codebase** — built for CLI, ready for web migration

---

## 🧱 System Design Overview

This system is built around the principle of **role-based access control**:

- **Admins** can:
  - View all members and their packages
  - Enforce rules about activity access based on membership
  - Use member statistics to make business decisions (e.g. adding equipment)
- **Members** can:
  - Log in securely
  - View and manage their membership package
  - Know exactly what facilities they are entitled to use
