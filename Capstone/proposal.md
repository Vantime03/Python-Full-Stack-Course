# Peer-to-Peer Tool Lending

## Project Overview

The purpose of this project is to create a peer-to-peer tool lending site. This site will allow users to lend their tools to others at a very low cost.

What's the benefit of peer-to-peer tool lending program? Here are the benefits: 
    (1) Cost of renting a tool can be lower comparing to other local tool rental companies.
    (2) Tool owners can make extra money from renting out their tools. 
    (3) You can still lend tools to your friends or family with this system. With this system, you have them accountable for what they're borrowing. 

## Project Scope

The scope of this project will consist of the following functional requirments: 

1. Allow new users (lenders or borrowers) to register accounts. 
2. Allow users (borrowers or lenders) to Logon and Logoff. 
3. Allow borrowers to search equipment from the equipment database for renting. 
4. Allow borrowers to request an equipment for rent. 
4. Allow lenders to upload equipment to the equipment database for leasing. Provide suggested leasing price based on the existing market
5. Allow lenders to accept the rental request. 
5. Create Equipment database table that shows a list of equipment for rent.
6. Create Transaction database table that shows all current and historical transactions.
7. Create User database table that contain user's profile information.

## Data model

The data model diagram for this project consist of 4 tables: 

- Borrower: contains  borrowers' information
- Lender: contains lenders' information
- Equipment: contains tools' information that associate with owner/lender and borrower
- Transaction: contains borrower, lender, and equipment information on each transaction

See the illustrate below for more details. 

![sample](screenshot_for_ERD.png)

## Schedule

The following tasks and milestones for this project will be completed by each week: 

Week 1 & 2: Database and Credentialize
- Build a database using SQL Lite (recommended by Justin, The Instructor)
- Build "Register Account" Function
- Build "Log On/Off" Function

Week 2 & 3: Upload Equipment to Database for Rent
- Buid a function that allows Lenders to upload tools to database for rent
    - this function will allow user to upload pictures of the tools, add descriptions and tools information 
    - This functions will also help user determine the approriate rent cost.
        | Tool Conditions        | Lease Percentrage    | MSRP Price  | Rent Price (MSRP Price x Lease Percentage) |
        | -----------------------|:--------------------:| -----------:| -----------------------------------------: |
        | Excellent              | 3%                   | $100        | $3                                         |
        | Good                   | 2%                   | $100        | $2                                         |
        | Average                | 1%                   | $100        | $1                                         |

Week 4: Search Equipment from Database to Rent and Send Rental Request
- Build a function that allows borrower to search equipment for rent. 
- Build a function that allows borrower to send a rent request to lender.

Week 5 & 6: Accept Rental Request
- Build a function that allows Lender to accept or reject rental request. 
    - when a lender accept: lender can send borrower a notification of pickup address, pickup time & date, return time & date, and total cost. 
    - when a lender reject: an automatic message will notify user.

Week 7: Payment System
- As of now payment system is cash.
- A potential API is still need to be determined.
    - https://developer.squareup.com/us/en?country_redirection=true 



Questions to make system better:
- What happend after the rental request is accepted? Where do both parties supposed to meet up to pick up tool? 
    - Answer: When borrower sends the rental request, the borrowers understand that they will have to pick up the tool at the Lender's address or within Lender's approximate location. When the lender accepts the rental request, they understand that the borrowers will pickup the tools at their addresses or within the approximation of their addresses. Upon accepting the rental request, Lender can disclose the pickup address, pickup time and date, return time and date, and total cost. 
    











