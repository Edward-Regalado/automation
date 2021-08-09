# Lab 19 - Automation

### Author

- **Tony Regalado**

### Code

[Code](https://github.com/Edward-Regalado/automation)

[Pull Request](https://github.com/Edward-Regalado/automation/pull/2)

### Overview

- Automate the process of looking through phone numbers and email addresses and edit the list of phone numbers so they fit a specific format.

### Featured Task & Requirments

- [x] Given a document **potential-contacts**, find and collect all email addresses and phone numbers.
- [x] Phone numbers may be in various formats.
    - [x] (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
    - [x] phone numbers with missing area code should presume 206
    - [x] phone numbers should be stored in xxx-yyy-zzzz format.
- [x] Once emails and phone numbers are found they should be stored in two separate documents.
- [x] The information should be sorted in ascending order.
- [x] Duplicate entries are not allowed.


### Implementation Notes

### User Acceptance Tests

- The ‘phone_numbers.txt’ and ‘emails.txt’ files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

### Stretch Goals

- [o] It turns out some of the contacts are already in our system.
- [o] Compare your collected data against existing-contacts.txt and only include info NOT already in system.
- [o] Handle phone numbers with extensions. E.g. (123) 456-789x012

### Configuration

- Use `poetry` to create `automation` project.
- Use the folder created by Poetry as the root of your project's git repository
- Refer to [Lab Submission Instructions](https://codefellows.github.io/code-401-python-guide/reference/submission-instructions/labs/) for detailed instructions.

### Collab & Credit 

- Kevin Henry & Anthony Williams. 

[w3Schools](https://www.w3schools.com/python/ref_string_split.asp)

[GeeksforGeeks](https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/)
