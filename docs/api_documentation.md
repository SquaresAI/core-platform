# API Documentation

## Overview
This document outlines the endpoints available in the `core-platform` API. The API is designed to support user management, AI workflows, and blockchain integrations, adhering to RESTful standards.

---

## Authentication Endpoints

### `/auth/login`
**Method**: POST  
**Description**: Authenticate a user and return a JWT token.  
**Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```
**Response**:
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

### `/auth/register`
**Method**: POST  
**Description**: Register a new user.  
**Request Body**:
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```
**Response**:
```json
{
  "id": "integer",
  "username": "string",
  "email": "string"
}
```

---

## User Management Endpoints

### `/users/`
**Method**: GET  
**Description**: Fetch a list of all users.  
**Response**:
```json
[
  {
    "id": "integer",
    "username": "string",
    "email": "string"
  }
]
```

---

## Blockchain Endpoints

### `/blockchain/transaction`
**Method**: POST  
**Description**: Initiate a blockchain transaction on Solana.  
**Request Body**:
```json
{
  "user_id": "integer",
  "transaction_data": "string"
}
```
**Response**:
```json
{
  "status": "string",
  "transaction_id": "string"
}
```

---

## AI Workflow Endpoints

### `/ai/models/`
**Method**: GET  
**Description**: List all available AI models.  
**Response**:
```json
[
  {
    "model_id": "integer",
    "model_name": "string",
    "status": "string"
  }
]
```
