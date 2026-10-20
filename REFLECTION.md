# Part B: Reflection

## 1. Test count and production code

Part A has 11 tests and 39 lines of production code, excluding blank lines and
comments. The ratio is 11:39, or about one test per 3.55 lines.

## 2. The longest red bar

I am not sure which red bar lasted longest because I did not time it. I think A7
was the hardest part because mixed-unit addition needed changes in `Converter`,
`Quantity.reduce` and `Sum.reduce`.

## 3. Fake It, Triangulate and Obvious Implementation

Fake It returned `600` in A1 to check the first test. Triangulation in A2 added
multiplication by two, forcing a real formula. Obvious Implementation in A3
returned a new `Quantity`. These choices worked well because each change was small.

## 4. Remaining items on the test list

All required items and A8 are finished. Hashability is still deferred; I would
remove it from the active list until dictionary keys are needed. Next, I would
test what happens when a conversion rate is missing.

## 5. Designing Quantity.reduce in advance

Probably not. I would likely put conversion in `Converter` first. The tests showed
why `Quantity` and `Sum` both need a `reduce` method.

## 6. Tests after code versus tests before code

Part 0 was about checking existing code using inputs and expected answers. Part A
was more about building behavior from tests. A3 changed multiplication to return
new objects, while A6-A7 shaped `Sum` and the shared reduction methods.
