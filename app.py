import streamlit as st
import datetime
import textwrap

# ============================================================
# SMART LIBRARY SYSTEM
# Python + Streamlit
# ============================================================

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# BOOK CLASS & ENHANCED MODEL
# ============================================================

class Book:
    def __init__(self, book_id, title, author, category="Fiction", rating=4.5, cover_emoji="📘", cover_color="#E8F0FE"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.rating = rating
        self.cover_emoji = cover_emoji
        self.cover_color = cover_color
        
        # Status tracking
        self.available = True
        self.issued_to = None
        self.issue_date = None
        self.due_date = None


# ============================================================
# BST NODE & BINARY SEARCH TREE
# ============================================================

class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BookBST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        new_node = BSTNode(book)
        if self.root is None:
            self.root = new_node
            return True
        current = self.root
        while True:
            if book.book_id < current.book.book_id:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            elif book.book_id > current.book.book_id:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
            else:
                return False

    def search(self, book_id):
        current = self.root
        while current is not None:
            if book_id == current.book.book_id:
                return current.book
            elif book_id < current.book.book_id:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self, node, result):
        if node is not None:
            self.inorder(node.left, result)
            result.append(node.book)
            self.inorder(node.right, result)


# ============================================================
# SEARCHING & SORTING ALGORITHMS
# ============================================================

def linear_search(books, title):
    return [book for book in books if title.lower() in book.title.lower()]

def binary_search(books, book_id):
    low = 0
    high = len(books) - 1
    while low <= high:
        mid = (low + high) // 2
        if books[mid].book_id == book_id:
            return books[mid]
        elif books[mid].book_id < book_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def bubble_sort(books):
    arr = books.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j].book_id > arr[j + 1].book_id:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(books):
    arr = books.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j].title.lower() < arr[min_index].title.lower():
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def merge_sort(books):
    if len(books) <= 1:
        return books.copy()
    middle = len(books) // 2
    left = merge_sort(books[:middle])
    right = merge_sort(books[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i].author.lower() <= right[j].author.lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def build_bst():
    bst = BookBST()
    for book in st.session_state.books:
        bst.insert(book)
    return bst


# ============================================================
# INITIAL BOOK DATA (50+ Books)
# ============================================================

if "books" not in st.session_state:
    st.session_state.books = [
        # Technology
        Book(101, "Data Structures", "Mark Allen", "Technology", 4.8, "💻", "#F7F5F0"),
        Book(102, "Computer Networks", "Andrew Tanenbaum", "Technology", 4.6, "🌐", "#F7F5F0"),
        Book(103, "Database Systems", "Raghu Ramakrishnan", "Technology", 4.7, "🗄️", "#F7F5F0"),
        Book(107, "Operating Systems", "Abraham Silberschatz", "Technology", 4.5, "⚙️", "#F7F5F0"),
        Book(209, "Design Patterns", "Erich Gamma", "Technology", 4.5, "🧩", "#F7F5F0"),
        Book(301, "Code Complete", "Steve McConnell", "Technology", 4.9, "🏗️", "#F7F5F0"),
        Book(302, "The Mythical Man-Month", "Fred Brooks", "Technology", 4.6, "📅", "#F7F5F0"),
        Book(303, "Introduction to Algorithms", "Thomas H. Cormen", "Technology", 4.7, "📐", "#F7F5F0"),
        
        # Programming
        Book(105, "Python Programming", "John Smith", "Programming", 4.9, "🐍", "#F7F5F0"),
        Book(207, "Clean Code", "Robert C. Martin", "Programming", 4.8, "🧹", "#F7F5F0"),
        Book(208, "The Pragmatic Programmer", "Andy Hunt", "Programming", 4.7, "🛠️", "#F7F5F0"),
        Book(304, "Effective Java", "Joshua Bloch", "Programming", 4.8, "☕", "#F7F5F0"),
        Book(305, "JavaScript: The Good Parts", "Douglas Crockford", "Programming", 4.4, "📜", "#F7F5F0"),
        Book(306, "Eloquent JavaScript", "Marijn Haverbeke", "Programming", 4.7, "🌐", "#F7F5F0"),
        Book(307, "Head First Design Patterns", "Eric Freeman", "Programming", 4.6, "🧠", "#F7F5F0"),
        Book(308, "Fluent Python", "Luciano Ramalho", "Programming", 4.9, "🐍", "#F7F5F0"),
        Book(309, "Rust Programming", "Steve Klabnik", "Programming", 4.8, "🦀", "#F7F5F0"),
        
        # AI & Science
        Book(108, "Machine Learning", "Tom Mitchell", "Science", 4.9, "🤖", "#F7F5F0"),
        Book(110, "Artificial Intelligence", "Andrew Ng", "Science", 5.0, "🧠", "#F7F5F0"),
        Book(205, "Sapiens", "Yuval Noah Harari", "Science", 4.6, "🧬", "#F7F5F0"),
        Book(310, "A Brief History of Time", "Stephen Hawking", "Science", 4.8, "⏳", "#F7F5F0"),
        Book(311, "Cosmos", "Carl Sagan", "Science", 4.9, "🌌", "#F7F5F0"),
        Book(312, "The Selfish Gene", "Richard Dawkins", "Science", 4.7, "🧬", "#F7F5F0"),
        Book(313, "Deep Learning", "Ian Goodfellow", "Science", 4.8, "🕸️", "#F7F5F0"),
        Book(314, "Grit", "Angela Duckworth", "Science", 4.5, "💪", "#F7F5F0"),
        
        # Fiction
        Book(201, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 4.3, "🥂", "#F7F5F0"),
        Book(202, "To Kill a Mockingbird", "Harper Lee", "Fiction", 4.9, "🏛️", "#F7F5F0"),
        Book(211, "The Alchemist", "Paulo Coelho", "Fiction", 4.4, "✨", "#F7F5F0"),
        Book(315, "1984", "George Orwell", "Fiction", 4.8, "👁️", "#F7F5F0"),
        Book(316, "Pride and Prejudice", "Jane Austen", "Fiction", 4.7, "💌", "#F7F5F0"),
        Book(317, "The Catcher in the Rye", "J.D. Salinger", "Fiction", 4.2, "🧢", "#F7F5F0"),
        Book(318, "The Lord of the Rings", "J.R.R. Tolkien", "Fiction", 4.9, "💍", "#F7F5F0"),
        Book(319, "Harry Potter", "J.K. Rowling", "Fiction", 4.8, "⚡", "#F7F5F0"),
        Book(320, "The Hobbit", "J.R.R. Tolkien", "Fiction", 4.7, "🐉", "#F7F5F0"),
        Book(321, "Fahrenheit 451", "Ray Bradbury", "Fiction", 4.6, "🔥", "#F7F5F0"),
        
        # Biography
        Book(210, "Steve Jobs", "Walter Isaacson", "Biography", 4.6, "🍎", "#F7F5F0"),
        Book(322, "Elon Musk", "Ashlee Vance", "Biography", 4.5, "🚀", "#F7F5F0"),
        Book(323, "Becoming", "Michelle Obama", "Biography", 4.8, "🌟", "#F7F5F0"),
        Book(324, "The Diary of a Young Girl", "Anne Frank", "Biography", 4.7, "📓", "#F7F5F0"),
        Book(325, "Long Walk to Freedom", "Nelson Mandela", "Biography", 4.9, "🕊️", "#F7F5F0"),
        Book(326, "Einstein", "Walter Isaacson", "Biography", 4.7, "⚛️", "#F7F5F0"),
        Book(327, "Shoe Dog", "Phil Knight", "Biography", 4.8, "👟", "#F7F5F0"),
        
        # Self-Help
        Book(206, "Atomic Habits", "James Clear", "Self-Help", 4.9, "📈", "#F7F5F0"),
        Book(328, "Thinking, Fast and Slow", "Daniel Kahneman", "Self-Help", 4.7, "🧠", "#F7F5F0"),
        Book(329, "The Power of Habit", "Charles Duhigg", "Self-Help", 4.6, "🔄", "#F7F5F0"),
        Book(330, "Mindset", "Carol S. Dweck", "Self-Help", 4.6, "🌱", "#F7F5F0"),
        Book(331, "How to Win Friends", "Dale Carnegie", "Self-Help", 4.8, "🤝", "#F7F5F0"),
        Book(332, "The Subtle Art", "Mark Manson", "Self-Help", 4.3, "🖕", "#F7F5F0"),
        Book(333, "Deep Work", "Cal Newport", "Self-Help", 4.7, "🎧", "#F7F5F0"),
        
        # Arts
        Book(334, "The Story of Art", "E.H. Gombrich", "Arts", 4.8, "🎨", "#F7F5F0"),
        Book(335, "Ways of Seeing", "John Berger", "Arts", 4.6, "👁️", "#F7F5F0"),
        Book(336, "Steal Like an Artist", "Austin Kleon", "Arts", 4.7, "✍️", "#F7F5F0"),
        Book(337, "The Creative Act", "Rick Rubin", "Arts", 4.9, "🌊", "#F7F5F0")
    ]

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"


# ============================================================
# CUSTOM CSS FOR BEIGE/BLACK/WHITE UI
# ============================================================

st.markdown("""
<style>
    /* Global Styles & Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif !important;
        background-color: #F7F5F0 !important;
        color: #000000 !important;
    }
    
    .stApp > header {
        background-color: transparent !important;
    }

    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #000000 !important;
    }
    
    /* Enforce Black Text Everywhere */
    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: #000000 !important;
    }

    /* Top Navigation Area */
    .app-header {
        text-align: center;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    
    .app-title {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Cards */
    .book-card {
        background: #FFFFFF !important;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        border: 2px solid #000000;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .book-card:hover {
        transform: translateY(-5px);
        box-shadow: 4px 4px 0px rgba(0,0,0,1);
    }

    .book-cover {
        width: 80px;
        height: 110px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px;
        flex-shrink: 0;
        border: 2px solid #000000;
        background-color: #F7F5F0 !important;
    }

    .book-info {
        flex-grow: 1;
    }

    .book-title {
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 4px;
    }

    .book-author {
        font-size: 14px;
        font-weight: 500;
        margin-bottom: 8px;
    }
    
    .book-meta {
        font-size: 13px;
        display: flex;
        gap: 15px;
        align-items: center;
        font-weight: 500;
    }
    
    .book-rating {
        font-weight: 800;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    .status-badge {
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 800;
        border: 2px solid #000000;
    }
    .status-available { background: #FFFFFF; color: #000000; }
    .status-issued { background: #000000; color: #FFFFFF !important; }

    /* Issue Details Card */
    .issue-details {
        background: #F7F5F0;
        border-left: 4px solid #000000;
        padding: 12px 15px;
        border-radius: 8px;
        margin-top: 10px;
        font-size: 13px;
        font-weight: 500;
    }
    
    /* Override Streamlit Buttons to look like Categories */
    .stButton > button {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        color: #000000 !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        height: auto !important;
        transition: all 0.2s !important;
    }
    .stButton > button:hover {
        background-color: #F7F5F0 !important;
        box-shadow: 4px 4px 0px rgba(0,0,0,1) !important;
        transform: translateY(-2px) !important;
    }
    .stButton > button:active {
        box-shadow: 0px 0px 0px rgba(0,0,0,1) !important;
        transform: translateY(2px) !important;
    }
    
</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPER COMPONENTS
# ============================================================

def render_book_card(book):
    status_class = "status-available" if book.available else "status-issued"
    status_text = "Available" if book.available else "Issued"
    
    issue_html = ""
    if not book.available:
        issue_html = f"<div class='issue-details'><b>Issued to:</b> {book.issued_to} <br/><b>Due:</b> {book.due_date.strftime('%b %d, %Y')}</div>"
        
    # We must ensure there is absolutely no leading whitespace before the div tags 
    # so that Streamlit's markdown parser doesn't treat it as a code block!
    html = f"<div class='book-card'><div class='book-cover'>{book.cover_emoji}</div><div class='book-info'><div style='display: flex; justify-content: space-between; align-items: flex-start;'><div><div class='book-title'>{book.title}</div><div class='book-author'>by {book.author}</div></div><div class='status-badge {status_class}'>{status_text}</div></div><div class='book-meta'><span class='book-rating'>★ {book.rating}</span><span>•</span><span>{book.category}</span><span>•</span><span>ID: {book.book_id}</span></div>{issue_html}</div></div>"
    
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# NAVIGATION & SIDEBAR
# ============================================================

st.sidebar.markdown('<div style="font-size: 20px; font-weight: 800; text-align: center; margin-bottom: 20px;">LMS DESIGN</div>', unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🔍 Browse & Search", "🔄 Issue & Return", "👤 My Account", "⚙️ Admin (BST & Data)"],
    label_visibility="hidden"
)

st.sidebar.divider()
st.sidebar.caption("Smart Library System v2.0")


# ============================================================
# 1. HOME DASHBOARD
# ============================================================

if menu == "🏠 Home":
    st.markdown('<div class="app-header"><div class="app-title">Library Management System</div></div>', unsafe_allow_html=True)
    
    st.markdown("### Categories")
    
    cat_cols = st.columns(7)
    categories = ["All", "Fiction", "Science", "Technology", "Programming", "Biography", "Self-Help"]
    
    for i, cat in enumerate(categories):
        with cat_cols[i % 7]:
            if st.button(cat, use_container_width=True):
                st.session_state.selected_category = cat
                st.rerun()
                
    st.markdown(f"### Books in: {st.session_state.selected_category}")
    
    # Filter books
    filtered_books = st.session_state.books
    if st.session_state.selected_category != "All":
        filtered_books = [b for b in st.session_state.books if b.category == st.session_state.selected_category]
        
    # Sort books by rating (descending) to get top picks for the selected category
    top_books = sorted(filtered_books, key=lambda x: x.rating, reverse=True)
    
    if not top_books:
        st.info(f"No books found in the {st.session_state.selected_category} category.")
    else:
        col1, col2 = st.columns(2)
        for i, book in enumerate(top_books):
            if i % 2 == 0:
                with col1:
                    render_book_card(book)
            else:
                with col2:
                    render_book_card(book)


# ============================================================
# 2. BROWSE & SEARCH
# ============================================================

elif menu == "🔍 Browse & Search":
    st.markdown('<div class="app-header"><div class="app-title">Browse Library</div></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input("Search Books", placeholder="Enter title, author, or keyword...", label_visibility="collapsed")
    with col2:
        sort_by = st.selectbox("Sort By", ["Title (A-Z)", "Author (A-Z)", "Book ID", "Highest Rating"], label_visibility="collapsed")
        
    st.divider()
    
    display_list = st.session_state.books.copy()
    
    if sort_by == "Book ID":
        display_list = bubble_sort(display_list)
    elif sort_by == "Title (A-Z)":
        display_list = selection_sort(display_list)
    elif sort_by == "Author (A-Z)":
        display_list = merge_sort(display_list)
    elif sort_by == "Highest Rating":
        display_list = sorted(display_list, key=lambda x: x.rating, reverse=True)
        
    if search_query:
        display_list = linear_search(display_list, search_query)
        st.markdown(f"**Found {len(display_list)} results for '{search_query}'**")
        
    if not display_list:
        st.warning("No books matched your search.")
    else:
        c1, c2 = st.columns(2)
        for i, book in enumerate(display_list):
            if i % 2 == 0:
                with c1:
                    render_book_card(book)
            else:
                with c2:
                    render_book_card(book)


# ============================================================
# 3. ISSUE & RETURN (ENHANCED WORKFLOWS)
# ============================================================

elif menu == "🔄 Issue & Return":
    st.markdown('<div class="app-header"><div class="app-title">Issue & Return Books</div></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📤 Issue Book", "📥 Return Book"])
    
    bst = build_bst()
    
    with tab1:
        st.markdown("### Issue a Book to a Student/User")
        
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                book_id_issue = st.number_input("Enter Book ID", min_value=1, step=1, key="issue_id")
                issue_duration = st.selectbox("Loan Duration", ["7 Days", "14 Days", "30 Days"])
            with col2:
                student_name = st.text_input("Borrower Full Name", placeholder="e.g. John Doe")
                
            if st.button("Issue Book", type="primary", use_container_width=True):
                if not student_name:
                    st.error("❌ Please provide the borrower's name.")
                else:
                    book = bst.search(int(book_id_issue))
                    if book is None:
                        st.error("❌ Book ID not found in library.")
                    elif not book.available:
                        st.error(f"❌ '{book.title}' is currently issued to {book.issued_to}.")
                    else:
                        days = int(issue_duration.split(" ")[0])
                        
                        book.available = False
                        book.issued_to = student_name
                        book.issue_date = datetime.date.today()
                        book.due_date = datetime.date.today() + datetime.timedelta(days=days)
                        
                        st.success(f"✅ Successfully issued '{book.title}' to {student_name}.")
                        st.balloons()
                        st.rerun()

    with tab2:
        st.markdown("### Return a Book")
        
        with st.container(border=True):
            book_id_return = st.number_input("Enter Book ID to Return", min_value=1, step=1, key="return_id")
            
            if st.button("Process Return", type="primary", use_container_width=True):
                book = bst.search(int(book_id_return))
                if book is None:
                    st.error("❌ Book ID not found in library.")
                elif book.available:
                    st.warning("⚠️ This book is already marked as returned/available.")
                else:
                    overdue = False
                    if datetime.date.today() > book.due_date:
                        overdue = True
                        days_late = (datetime.date.today() - book.due_date).days
                        
                    borrower = book.issued_to
                    
                    book.available = True
                    book.issued_to = None
                    book.issue_date = None
                    book.due_date = None
                    
                    if overdue:
                        st.warning(f"✅ '{book.title}' returned by {borrower}. NOTE: This book was {days_late} days overdue.")
                    else:
                        st.success(f"✅ '{book.title}' returned successfully by {borrower} on time!")
                    st.rerun()


# ============================================================
# 4. MY ACCOUNT
# ============================================================

elif menu == "👤 My Account":
    st.markdown('<div class="app-header"><div class="app-title">My Account</div></div>', unsafe_allow_html=True)
    
    st.write("View books currently issued in the system.")
    
    issued_books = [b for b in st.session_state.books if not b.available]
    
    st.metric("Total Books Currently Borrowed", len(issued_books))
    
    if not issued_books:
        st.info("No books are currently issued out.")
    else:
        st.markdown("### Active Loans")
        for book in issued_books:
            render_book_card(book)


# ============================================================
# 5. ADMIN & BST VIEW
# ============================================================

elif menu == "⚙️ Admin (BST & Data)":
    st.markdown('<div class="app-header"><div class="app-title">System Administration</div></div>', unsafe_allow_html=True)
    
    st.write("This section demonstrates the underlying Data Structures and Algorithms.")
    
    tab1, tab2 = st.tabs(["🌳 BST Traversal", "➕ Add New Book"])
    
    with tab1:
        st.markdown("### Binary Search Tree")
        st.info("The BST stores books by Book ID. Performing an **Inorder Traversal** yields a sorted list by ID.")
        
        bst = build_bst()
        bst_books = []
        bst.inorder(bst.root, bst_books)
        
        table = []
        for b in bst_books:
            table.append({
                "ID": b.book_id,
                "Title": b.title,
                "Author": b.author,
                "Status": "Available" if b.available else f"Issued ({b.issued_to})"
            })
        st.dataframe(table, width='stretch', hide_index=True)
        
    with tab2:
        st.markdown("### Add Book to Database")
        with st.form("add_book_form"):
            c1, c2 = st.columns(2)
            with c1:
                b_id = st.number_input("Book ID", min_value=1, step=1)
                b_title = st.text_input("Title")
                b_author = st.text_input("Author")
            with c2:
                b_cat = st.selectbox("Category", ["Fiction", "Technology", "Programming", "Sci-Fi", "Science", "Biography", "Self-Help"])
                b_rate = st.slider("Initial Rating", 1.0, 5.0, 4.5, 0.1)
                
            submitted = st.form_submit_button("Add to System", use_container_width=True)
            
            if submitted:
                bst = build_bst()
                if bst.search(int(b_id)):
                    st.error("❌ Book ID already exists!")
                elif not b_title or not b_author:
                    st.warning("⚠️ Title and Author are required.")
                else:
                    new_b = Book(int(b_id), b_title.strip(), b_author.strip(), b_cat, b_rate)
                    st.session_state.books.append(new_b)
                    st.success(f"✅ {b_title} added!")
                    st.rerun()

