# CV Parser taken from https://github.com/xitanggg/open-resume

Note from Yiji: Reading the CV is one of the hardest things to do, especially with all the different formats there are out there. We have adapted the code from [open-resume](https://github.com/xitanggg/open-resume) to save time on creating a resume parser. The following algorithm deep dive is adapted from the [original deep-dive here](https://www.open-resume.com/resume-parser#:~:text=Resume%20Parser%20Algorithm%20Deep%20Dive).

**The algorithm is best designed to parse a single column CV in PDF format in English language.**

# Resume Parser Algorithm Deep Dive

For the technical curious, this section will dive into the OpenResume parser algorithm and walks through the 4 steps on how it works.

## Step 1. Read the text items from a PDF file

A PDF file is a standardized file format defined by the [ISO 32000 specification](https://www.iso.org/standard/51502.html). When you open up a PDF file using a text editor, you'll notice that the raw content looks encoded and is difficult to read. To display it in a readable format, you would need a PDF reader to decode and view the file. Similarly, the resume parser first needs to decode the PDF file in order to extract its text content.

While it is possible to write a custom PDF reader function following the ISO 32000 specification, it is much simpler to leverage an existing library. In this case, the resume parser uses Mozilla's open source [pdf.js](https://github.com/mozilla/pdf.js) library to first extract all the text items in the file.

The table below is an example of the text items that are extracted from the resume PDF added. A text item contains the text content and also some metadata about the content, e.g. its x, y positions in the document, whether the font is bolded, or whether it starts a new line. (Note that x,y position is relative to the bottom left corner of the page, which is the origin 0,0)

| # | Text Content | Metadata |
|-------------------|-------------------------------|-------------------------------|
| 1 | 2                        | X₁=569 X₂=576 Y=745        |
| 2 |                        | X=266 Y=729 Bold NewLine        |
| 3 | Leo Leopard                       | X₁=266 X₂=346 Y=729 Bold        |
| 4 |                        | X=224 Y=714 NewLine       |
| 5 | 555 La Verne Way,                       | X₁=224 X₂=320 Y=714        |
| 6 | La Verne, CA                 | X₁=323 X₂=388 Y=714       |


## Step 2. Group text items into lines

The extracted text items aren't ready to use yet and have 2 main issues:

**Issue 1: They have some unwanted noises.** Some single text items can get broken into multiple ones, e.g. a phone number "(123) 456-7890" might be broken into 3 text items "(123) 456", "-" and "7890".

**Solution:** To tackle this issue, the resume parser connects adjacent text items into one text item if their distance is smaller than the average typical character width, where

```
Distance = RightTextItemX₁ - LeftTextItemX₂
```

The average typical character width is calculated by dividing the sum of all text items' widths by the total number characters of the text items (Bolded texts and new line elements are excluded to not skew the results).

**Issue 2: They lack contexts and associations.** When we read a resume, we scan a resume line by line. Our brains can process each section via visual cues such as texts' boldness and proximity, where we can quickly associate texts closer together to be a related group. The extracted text items however currently don't have those contexts/associations and are just disjointed elements.

**Solution:** To tackle this issue, the resume parser reconstructs those contexts and associations similar to how our brain would read and process the resume. It first groups text items into lines since we read text line by line. It then groups lines into sections, which will be discussed in the next step.

At the end of step 2, the resume parser extracts lines from the resume PDF added. The result is much more readable when displayed in lines. (Some lines might have multiple text items, which are separated by a blue vertical divider `|`)

## Step 3. Group lines into sections

At step 2, the resume parser starts building contexts and associations to text items by first grouping them into lines. Step 3 continues the process to build additional associations by grouping lines into sections.

Note that every section (except the profile section) starts with a section title that takes up the entire line. This is a common pattern not just in resumes but also in books and blogs. The resume parser uses this pattern to group lines into the closest section title above these lines.

The resume parser applies some heuristics to detect a section title. The main heuristic to determine a section title is to check if it fulfills all 3 following conditions:
1. It is the only text item in the line
2. It is **bolded**
3. Its letters are all UPPERCASE

In simple words, if a text item is double emphasized to be both bolded and uppercase, it is most likely a section title in a resume. This is generally true for a well formatted resume. There can be exceptions, but it is likely not a good use of bolded and uppercase in those cases.

The resume parser also has a fallback heuristic if the main heuristic doesn't apply. The fallback heuristic mainly performs a keyword matching against a list of common resume section title keywords.

At the end of step 3, the resume parser identifies the sections from the resume and groups those lines with the associated section title.

## Step 4. Extract resume from sections

Step 4 is the last step of the resume parsing process and is also the core of the resume parser, where it extracts resume information from the sections.

### Feature Scoring System

The gist of the extraction engine is a feature scoring system. Each resume attribute to be extracted has a custom feature sets, where each feature set consists of a feature matching function and a feature matching score if matched (feature matching score can be a positive or negative number). To compute the final feature score of a text item for a particular resume attribute, it would run the text item through all its feature sets and sum up the matching feature scores. This process is carried out for all text items within the section, and the text item with the highest computed feature score is identified as the extracted resume attribute.

In the resume PDF added, the resume attribute name is likely to be "[name]" since its feature score is [score], which is the highest feature score out of all text items in the profile section. (Some text items' feature scores can be negative, indicating they are very unlikely to be the targeted attribute)

### Feature Sets

Having explained the feature scoring system, we can dive more into how feature sets are constructed for a resume attribute. It follows 2 principles:
1. A resume attribute's feature sets are designed relative to all other resume attributes within the same section.
2. A resume attribute's feature sets are manually crafted based on its characteristics and likelihood of each characteristic.

The table below lists some of the feature sets for the resume attribute name. It contains feature function that matches the name attribute with positive feature score and also feature function that only matches other resume attributes in the section with negative feature score.

| Feature Function                                         | Feature Matching Score |
|----------------------------------------------------------|------------------------|
| Contains only letters, spaces or periods                | +3                     |
| Is bolded                                                | +2                     |
| Contains all uppercase letters                           | +2                     |
| Contains @                                               | -4 (match email)       |
| Contains number                                          | -4 (match phone)       |
| Contains ,                                               | -4 (match address)     |
| Contains /                                               | -4 (match url)         |

### Core Feature Function

Each resume attribute has multiple feature sets. They can be found in the source code under the extract-resume-from-sections folder and we won't list them all out here. Each resume attribute usually has a core feature function that greatly identifies them, so we will list out the core feature function below.

| Resume Attribute | Core Feature Function                                | Regex                                   |
|-------------------|--------------------------------------------------------|------------------------------------------|
| Name              | Contains only letters, spaces or periods              | `/^[a-zA-Z\s\.]+$/`                     |
| Email             | Match email format xxx@xxx.xxx <br /> xxx can be anything not space | `/\S+@\S+\.\S+/`                         |
| Phone             | Match phone format (xxx)-xxx-xxxx <br /> () and - are optional | `/\(?\\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}/` |
| Location          | Match city and state format "City, ST"                 | `/[A-Z][a-zA-Z\s]+, [A-Z]{2}/`           |
| Url               | Match url format xxx.xxx/xxx                           | `/\S+\.[a-z]+\/\S+/`                    |
| School            | Contains a school keyword, e.g. College, University, School | -                                        |
| Degree            | Contains a degree keyword, e.g. Associate, Bachelor, Master | -                                        |
| GPA               | Match GPA format x.xx                                  | `/[0-4]\.\d{1,2}/`                       |
| Date              | Contains date keyword related to year, month, seasons or the word Present | Year: `/


### Special case: Subsections
The last thing that is worth mentioning is subsections. For profile section, we can directly pass all the text items to the feature scoring systems. But for other sections, such as education and work experience, we have to first divide the section into subsections since there can be multiple schools or work experiences in the section. The feature scoring system then process each subsection to retrieve each's resume attributes and append the results.

The resume parser applies some heuristics to detect a subsection. The main heuristic to determine a subsection is to check if the vertical line gap between 2 lines is larger than the typical line gap * 1.4, since a well formatted resume usually creates a new empty line break before adding the next subsection. There is also a fallback heuristic if the main heuristic doesn't apply to check if the text item is bolded.