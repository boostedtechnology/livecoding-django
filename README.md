# livecoding-django


To get started on Mac, assuming Python is already installed:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
``` 

To confirm everything is working, run `python3 manage.py test core.tests.accounts` to make sure the base functionality it working.

The other test files are defined but should not work until you implement the tasks.

## Task 1: Implement DELETE /accounts/:id/ endpoint

We want to be able to delete an account by its ID. Add a new endpoint to the controller to delete an account by its ID.

Run `python3 manage.py test core.tests.task_1` to test if it works.


## Task 2: Implement POST /transactions/

**Context**

A transaction in double-entry accounting is a record of a financial transaction. Each transaction has a description and a list of entries. Each entry has an account ID, a debit amount, and a credit amount. Within a transaction, the sum of the debit amounts must equal the sum of the credit amounts. There must be at least two entries in a transaction.

**Task**

Create the service, controller, and routes for the POST /transactions/ endpoint.

You can decide how to structure the request body, but the following is potential example
that shows a transaction with three account entries on the transaction.

```json
{
  "description": "Office supplies at Staples",
  "entries": [
    {
      "accountId": "a018f63f-3794-4927-90fa-b62f26892203",
      "type": "DEBIT",
      "amount": 12456
    },
    {
      "accountId": "ee51e463-f4f9-4ddf-a2b3-af8e196f851f",
      "type": "CREDIT",
      "amount": 10000
    },
    {
      "accountId": "d9e645c9-ff24-4360-9cde-c31fcffa76dc",
      "type": "CREDIT",
      "amount": 2456
    }
  ]
}
```

* Only worry about the POST endpoint for now. The other CRUD operations do not need to be implemented.

* The models are already created for Transaction and TransactionEntry, but feel free to modify / delete them as desired.

Run `python3 manage.py test core.tests.task_2` to test if it works.


## Task 3: Add a `balance` field to the response of GET /accounts/:id/

**Context**

Each account has a "balance" based on the transactions involving the account.

* For Asset and Expense accounts, the balance is the sum of all the debit entries involving the account minus the sum of all the credit entries involving the account.
* For Liability, Equity, and Revenue accounts, the balance is the sum of all the credit entries involving the account minus the sum of all the debit entries involving the account.

Run `python3 manage.py test core.tests.task_3` to test if it works.

**Task**

On the response of GET /accounts/:id/, add a `balance` field on the response.


## Task 4: Convert the DELETE /accounts/:id/ endpoint to use a soft delete

Update the DELETE /accounts/:id endpoint to prevent the deletion of accounts used in any transactions.

In short, this should not delete the record from the database, but instead put the record in a "deactivated" state. In this deleted state, you should still be able to see the
account in the GET /accounts/:id/ endpoint, but it should not be included in the GET /accounts/ endpoint or be usable in the POST /transactions/ endpoint as an entry.

Create your own test suite for this task.
