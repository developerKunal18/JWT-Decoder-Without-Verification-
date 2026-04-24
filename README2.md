# JWT Decoder

A Python script that decodes JWT header and payload.

## Description
This project helps inspect JWT tokens by decoding the Base64URL encoded header and payload.

> Note: This tool does not verify signatures.

## Features
- Decode JWT header
- Decode JWT payload
- Pretty JSON output
- Useful for API debugging

## Technologies Used
- Python
- base64 module
- json module

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run:

   python jwt_decoder.py

4. Enter JWT token

## Example

Output:
Header:
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload:
{
  "sub": "123",
  "name": "John"
}

## Purpose
This project is part of my daily coding challenge.
Day 194 focuses on authentication tooling and data decoding.
