<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>

<h1>Flight Route Management System</h1>

<p>
This project is a <strong>Django-based Flight Route Management System</strong> that
models airport routes using a tree structure. Airports can be added as root nodes
or as left/right child nodes, and various route-based operations can be performed.
</p>

<div class="section">
    <h2>Features</h2>
    <ul>
        <li>Add root airports and child airports (left or right)</li>
        <li>Prevent duplicate left/right child positions</li>
        <li>Find the Nth airport by traversing left or right</li>
        <li>Find the airport with the longest duration</li>
        <li>Find the shortest route between two airports</li>
    </ul>
</div>

<div class="section">
    <h2>Project Structure</h2>
    <pre>
Flight_Route/
│
├── routes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── routes/
│           ├── add_airport.html
│           ├── nth_node.html
│           ├── longest_route.html
│           └── shortest_node.html
│
├── manage.py
├── requirements.txt
└── README.html
    </pre>
</div>

<div class="section">
    <h2>Airport Model</h2>
    <ul>
        <li><strong>airport_code</strong> – Airport identifier (e.g., DEL, DXB)</li>
        <li><strong>duration</strong> – Duration from the parent airport</li>
        <li><strong>parent</strong> – Reference to another airport (tree structure)</li>
        <li><strong>position</strong> – Left or Right child</li>
    </ul>
    <p>
        This structure allows airports to behave like a binary tree.
    </p>
</div>

<div class="section">
    <h2>Technologies Used</h2>
    <ul>
        <li>Python 3</li>
        <li>Django 5.x</li>
        <li>SQLite (default Django database)</li>
        <li>HTML (Django Templates)</li>
        <li>Bootstrap (basic styling)</li>
    </ul>
</div>

<div class="section">
    <h2>Installation Guide</h2>

  <h3>1. Clone the Repository</h3>
    <pre>
git clone &lt;repository-url&gt;
cd Flight_Route
    </pre>

  <h3>2. Create a Virtual Environment</h3>
    <pre>
python -m venv env
    </pre>

  <h3>3. Activate the Virtual Environment</h3>
    <pre>
Windows:
env\Scripts\activate

macOS / Linux:
source env/bin/activate
    </pre>

  <h3>4. Install Requirements</h3>
    <pre>
pip install -r requirements.txt
    </pre>

  <h3>5. Apply Database Migrations</h3>
    <pre>
python manage.py makemigrations
python manage.py migrate
    </pre>

  <h3>6. Run the Development Server</h3>
    <pre>
python manage.py runserver
    </pre>

  <p>
        Open your browser and go to:
        <strong>http://127.0.0.1:8000/</strong>
    </p>
</div>

<div class="section">
    <h2>Application URLs</h2>
    <table>
        <tr>
            <th>URL</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>/add/</td>
            <td>Add airport nodes (root / left / right)</td>
        </tr>
        <tr>
            <td>/nth/</td>
            <td>Find the Nth node by left/right traversal</td>
        </tr>
        <tr>
            <td>/longest/</td>
            <td>Display airport with the longest duration</td>
        </tr>
        <tr>
            <td>/shortest/</td>
            <td>Display the shortest route between two airports</td>
        </tr>
    </table>
</div>

<div class="section">
    <h2>How It Works</h2>
    <p>
        Root airports have no parent. Child airports represent routes between
        two airports, where duration defines the travel distance.
        The system automatically calculates shortest and longest routes
        based on stored data.
    </p>
</div>


</body>
</html>
