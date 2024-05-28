export default function Page() {
    return (
        <div>
        <h1>Resume Parser</h1>
        <p>
            This is a simple resume parser that parses a resume from a resume pdf file.
        </p>
        <p>
            Note: The parser algorithm only works for single column resume in English language.
        </p>
        <p>
            To parse a resume, please upload a resume pdf file.
        </p>
        <p>
            <input type="file" accept=".pdf" />
        </p>
        </div>
    );
    }
