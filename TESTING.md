# KICKIN' IT TESTING

Return back to the [README.md](README.md) file.

## Automated Testing

### HTML Validation

For HTML Validation I have used [HTML W3C Validator](https://validator.w3.org/)

All html files that includes Django templating language come back with errors, this is because the Validator does not recognise the Django templating language.

If the validation returns with only django template related errors, I am counting that as a Pass: No Errors.

| Page | Screenshot | Notes | Validation Status |
|:---|:---|:---|:---|
| Base | ![Base](documentaion/base-validation.png) | | Pass: No Errors |
| Home Page | ![Index Page](documentaion/index-validation.png)  | | Pass: No Errors |
| Products | ![Products](documentaion/product-validation.png) | | Pass: No Errors |
| Add Product | ![Add Product](documentaion/add-product-validation.png) | | Pass: No Errors |
| Edit Product | ![Edit Product](documentaion/edit-product-validation.png) | | Pass: No Errors |
| Product Details | ![Product Details](documentaion/product-detail-validation.png) | | Pass: No Errors |
| FAQ | ![FAQ](documentaion/faq-validation.png) | | Pass: No Errors |
| Checkout | ![Checkout](documentaion/checkout-validation.png) | | Pass: No Errors |
| Checkout Success | ![Checkout Success](documentaion/checkout-success-validation.png) | | Pass: No Errors |
| Bag | ![Bag](documentaion/bag-validation.png) | | Pass: No Errors |
| Wishlist | !![Wishlist](documentaion/wishlist-validation.png) | | Pass: No Errors |
| Newsletter Unsubscribe | ![Newsletter Unsub](documentaion/unsub-validation.png)| | Pass: No Errors |
| Newsletter  Unsub Confirmation | ![Newsletter Unsub Confirmation](documentaion/unsub-confirmation-validation.png)| | Pass: No Errors |
| Profile | ![Profile](documentaion/profile-validation.png)| | Pass: No Errors |

### CSS Validation

For CSS Validation I have used [CSS W3C Validator](https://jigsaw.w3.org/css-validator/)

| Page | Errors/Warnings | Notes | Validation Status |
|:---|:---|:---|:---|
| Base.css | None | | Pass: No Errors |
| Profiles.css | None | | Pass: No Errors |
| Checkout.css | None | | Pass: No Errors |

### JavaScript Validation

For JavaScript Validation I have used [JSHint](https://jshint.com/)

| Page |  Metrics | Warnings | Notes |
|:---|:---|:---|:---|
| stripe_elements.js | There are 5 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 10 statements in it, while the median is 5. The most complex function has a cyclomatic complexity value of 3 while the median is 1. | 2 Warnings for ES6 Template Literal Syntax 1 Warning for a missing semicolon, which has been fixed since. | Undefined Variables of $ all over the file, this is because jshint doesn't recognise JQuery |
| bag.html | There are 3 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 6 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 1 while the median is 1. | 1 Warning for ES6 Template Literal Syntax | JQuery Unrecognised |
| products.html | There are 2 functions in this file. Function with the largest signature take 1 arguments, while the median is 0.5. Largest function has 12 statements in it, while the median is 6.5. The most complex function has a cyclomatic complexity value of 2 while the median is 1.5.| No Warnings | JQuery Unrecognised |
| countryfield.js | There is only one function in this file. It takes no arguments. This function contains 4 statements. Cyclomatic complexity number for this function is 2. | "Let" ES6 warning | JQuery Unrecognised |

### Python Validation

For Python Validation I have used the Code Institute [Python Linter](https://pep8ci.herokuapp.com/) Any identifiied issues were fixed.

All .py files in all Apps came back with no errors.

### Lighthouse

I used Googles Lighthouse tool to test the site and identify any areas of improvement.

| Page | Mobile | Desktop | Notes |
|:---|:---|:---|:---|
| Landing Page | ✅ | ✅ | |

## Manual Testing

See last project feedback

## Responsive Design

<details>

<summary>Responsive Design</summary>


</details>

## User Story Testing

<details>

<summary>User Story Testing</summary>



</details>

## Defensive Programming

<details>

<summary>Defensive Programming</summary>

| | Expected | Test | Actual |
|:---|:---|:---|:---|
| | | | |

</details>

## Bugs
