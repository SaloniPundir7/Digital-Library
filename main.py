import json  #for specific format
import os    #for checking existence of json file
import docx
import webbrowser


JSON_FILE = "library.json"


class files:
    def __init__(self, name, category, genre, price, rating, access_type, writer, file_path=""):
        self.name = name
        self.category = category
        self.genre = genre
        self.price = price
        self.rating = rating
        self.access_type = access_type
        self.writer = writer
        self.file_path = file_path  # path to actual file

    def file(self):
     return (
        "\n" + "=" * 40 + "\n"
        f"Title       : {self.name}\n"
        f"Category    : {self.category}\n"
        f"Genre       : {', '.join(self.genre)}\n"
        f"Price       : {'Free' if self.price == 0 else self.price}\n"
        f"Rating      : {self.rating}/5\n"
        f"Access Type : {self.access_type.capitalize()}\n"
        f"Author      : {self.writer}\n"
        f"File Path   : {self.file_path}\n"
        + "=" * 40
    )

   

    def metadata(self):
        """Return only metadata for preview."""
        return (
            f"{self.name} ({self.category})\n"
            f"Genres: {', '.join(self.genre)} | "
            f"Price: {'Free' if self.price == 0 else self.price} | "
            f"Rating: {self.rating}/5 | "
            f"Author: {self.writer}"
    )


    def open(self):
      print(f"\nOpening '{self.name}'...\n")
      # OPEN WEB ARTICLES
      if self.file_path.startswith("http"):
        print("Opening article in web browser...")
        webbrowser.open(self.file_path)
        return


      if not self.file_path or not os.path.exists(self.file_path):
        print("⚠️ File not found.")
        return

    # SAFE extension detection
      _, ext = os.path.splitext(self.file_path)
      ext = ext.lower()

      try:
        # AUDIO FILES
        # AUDIO FILES
        if ext in [".mp3", ".wav"]:
           print("Opening audio in default media player...")
           os.startfile(self.file_path)
           input("Press Enter after closing audio player...")
           return


        # TEXT FILES
        elif ext == ".txt":
            with open(self.file_path, "r", encoding="utf-8") as f:
                print(f.read())

        # PDF FILES
        elif ext == ".pdf":
          print("Opening in default PDF viewer...")
          os.startfile(self.file_path)
          input("Press Enter after closing the PDF...")


        # WORD FILES (DOCX)
        elif ext == ".docx":
           choice = input("1. Read in terminal\n2. Open in Word\nChoose: ").strip()

           if choice == "1":
              doc = docx.Document(self.file_path)
              for para in doc.paragraphs:
                if para.text.strip():
                   print(para.text)

           elif choice == "2":
              print("Opening in Microsoft Word...")
              os.startfile(self.file_path)
              input("Press Enter after closing Word...")
              return   # 👈 THIS IS IMPORTANT

           else:
             print("Invalid choice.")

        else:
            print(f"⚠️ Unsupported file type: {ext}")

      except Exception as e:
        print(f"❌ Error opening file: {e}")



    def to_dict(self):
     return {
        "name": self.name,
        "category": self.category,
        "genre": self.genre,
        "price": self.price,
        "rating": self.rating,
        "access_type": self.access_type,
        "writer": self.writer,
        "file_path": self.file_path
    }

    @staticmethod
    def from_dict(data):
      return files(
         data.get("name", "Unknown"),
         data.get("category", "Unknown"),
         data.get("genre", []),
         data.get("price", 0),
         data.get("rating", 0),
         data.get("access_type", "user"),
         data.get("writer", "Unknown"),
         data.get("file_path", "")  # default to empty string
    )




def save_library(library):  #save mechanism
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([item.to_dict() for item in library], f, indent=4)


def load_library(default_library):
    try:
        if not os.path.exists(JSON_FILE):
            save_library(default_library)

        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [files.from_dict(item) for item in data]

    except (json.JSONDecodeError, KeyError) as e:
        print(f"⚠️ Error loading library: {e}")
        print("Loading default library instead.")
        return default_library


initial_library = [
    # Books
    files("The Silent Code", "Book", ["Technology"], 16, 4.5, "user", "James Carter","Here9.docx"),
    files("Echoes of Tomorrow", "Book", ["Science Fiction"], 19, 4.7, "user", "Lila Monroe"),
    files("Whispers in the Wind", "Book", ["Romance"], 13, 4.2, "user", "Nora Blake"),
    files("The Last Kingdom", "Book", ["History"], 20, 4.6, "user", "Arthur Collins"),
    files("Mind Over Matter", "Book", ["Self-Help"], 15, 4.3, "user", "Daniel Ross"),
    files("Shadow Realm", "Book", ["Fantasy"], 17, 4.8, "user", "Evelyn Storm"),
    files("Digital Fortress", "Book", ["Thriller"], 18, 4.4, "user", "Mark Evans"),
    files("The Art of Calm", "Book", ["Wellness"], 12, 4.1, "user", "Sophia Reed"),
    files("Broken Truths", "Book", ["Mystery"], 13, 4.0, "user", "Hannah Cole"),
    files("Infinite Paths", "Book", ["Philosophy"], 20, 4.6, "user", "Victor Hale"),
    files("Rising Tides", "Book", ["Adventure"], 15, 4.3, "user", "Leo Marshall"),
    files("The Coding Mind", "Book", ["Education"], 21, 4.7, "user", "Priya Nair"),
    files("Golden Ashes", "Book", ["Drama"], 15, 4.2, "user", "Rachel Moore"),
    files("Nightfall City", "Book", ["Crime"], 17, 4.5, "user", "Thomas Gray"),
    files("Beyond the Stars", "Book", ["Space"], 19, 4.8, "user", "Amelia Wright"),
    files("Hidden Signals", "Book", ["Technology"], 17, 4.4, "user", "Kevin Liu"),
    files("The Long Road Home", "Book", ["Fiction"], 14, 4.1, "user", "Michael Stone"),
    files("Fragments of Time", "Book", ["Time Travel"], 20, 4.6, "user", "Clara Bennett"),
    files("The Iron Will", "Book", ["Biography"], 22, 4.7, "user", "Samuel Ortiz"),
    files("Secrets of the Mind", "Book", ["Psychology"], 17, 4.5, "user", "Dr. Elaine Foster"),

    # Audiobooks
    files("The Power Within", "Audiobook", ["Self-Help"], 10, 4.6, "user", "Alan Brooks"),
    files("Voices of History", "Audiobook", ["History"], 12, 4.4, "user", "Margaret Lee"),
    files("Future Horizons", "Audiobook", ["Science Fiction"], 13, 4.7, "user", "Ian Cooper"),
    files("Calm Nights", "Audiobook", ["Wellness"], 9, 4.2, "user", "Laura Kim"),
    files("The Dark Alley", "Audiobook", ["Crime"], 11, 4.5, "user", "Robert Miles"),
    files("Think Smart", "Audiobook", ["Education"], 10, 4.3, "user", "Nina Patel"),
    files("Mystic Lands", "Audiobook", ["Fantasy"], 13, 4.8, "user", "Oliver Grant"),
    files("The Entrepreneur Way", "Audiobook", ["Business"], 15, 4.6, "user", "Steven Park"),
    files("Lost Frequencies", "Audiobook", ["Mystery"], 12, 4.4, "user", "Chloe Adams"),
    files("Deep Space Dreams", "Audiobook", ["Space"], 13, 4.7, "user", "Ethan Cole"),
    files("Mindful Living", "Audiobook", ["Wellness"], 9, 4.3, "user", "Sarah Lin"),
    files("Legends Reborn", "Audiobook", ["Adventure"], 14, 4.6, "user", "Paul Rivera"),
    files("The Inner Voice", "Audiobook", ["Psychology"], 11, 4.2, "user", "Dr. Megan Fox"),
    files("Code Stories", "Audiobook", ["Technology"], 11, 4.5, "user", "Andrew Zhao"),
    files("Echo Chamber", "Audiobook", ["Thriller"], 13, 4.4, "user", "Brian Scott"),
    files("Waves of Change", "Audiobook", ["Motivation"], 10, 4.3, "user", "Emily Turner"),
    files("The Ancient Scrolls", "Audiobook", ["History"], 14, 4.6, "user", "Victor Han"),
    files("Path to Success", "Audiobook", ["Career"], 11, 4.5, "user", "Linda Gomez"),
    files("Dreamstate", "Audiobook", ["Fiction"], 12, 4.1, "user", "Noah Price"),
    files("The Quiet Mind", "Audiobook", ["Meditation"], 9, 4.4, "user", "Zen Master Kai"),

    # Articles
    files("AI in Everyday Life", "Article", ["Technology"], 0, 4.5, "user", "Dr. Alex Morgan"),
    files("The Future of Work", "Article", ["Business"], 0, 4.3, "user", "Rachel Young"),
    files("Healthy Habits 101", "Article", ["Health"], 0, 4.1, "user", "Dr. Nina Shah"),
    files("Space Tourism Explained", "Article", ["Space"], 0, 4.6, "user", "Leo Carter"),
    files("Mental Health Matters", "Article", ["Psychology"], 0, 4.4, "user", "Olivia Brown"),
    files("Climate Change Today", "Article", ["Environment"], 0, 4.5, "user", "Daniel Green"),
    files("Cybersecurity Basics", "Article", ["Technology"], 0, 4.2, "user", "Kevin White"),
    files("Remote Learning Trends", "Article", ["Education"], 0, 4.3, "user", "Monica Lopez"),
    files("The Art of Focus", "Article", ["Productivity"], 0, 4.4, "user", "James Wilson"),
    files("Modern Relationships", "Article", ["Lifestyle"], 0, 4.1, "user", "Emma Davis")
]


initial_library = load_library(initial_library)


#search logic
def display_all_files(library):
    print("\n📚 LIBRARY CONTENTS\n")
    for item in library:
        print(item.file())



def search_by_title(library, access):
    title = get_non_empty_input("Enter title: ").lower()
    found = False

    for item in library:
        if title in item.name.lower() and access == item.access_type.lower():
            print("\nFile found:\n")
            print(item.file())
            # Ask user if they want to open it
            open_choice = input("Do you want to open this file? (y/n): ").strip().lower()
            if open_choice == "y":
                item.open()  # ⭐ call the class method
            found = True

    if not found:
        print("\nTitle not found.")




def search_by_genre(library, access):
    genre_input = get_non_empty_input("Enter genre to search: ").lower()
    genre_found = False

    for item in library:
        if genre_input in [g.lower() for g in item.genre] and access == item.access_type.lower():
            print("\nMatching file:\n")
            print(item.file())  # only metadata
            genre_found = True

            # ✅ Ask user to open file
            open_choice = input("Do you want to open this file? (y/n): ").strip().lower()
            if open_choice == "y":
                item.open()  # calls your open() method which handles terminal or Word

    if not genre_found:
        print("\nNo files found for this genre and access type.")


def display_library_metadata(library):
    print("\n📚 LIBRARY OVERVIEW (metadata only)\n")
    for idx, item in enumerate(library, start=1):
        print(f"{idx}. {item.metadata()}")

def show_full_file(library):
    choice = get_non_empty_input("Enter the number to see full details, or 0 to go back: ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(library):
            item = library[choice - 1]
            print(item.file())  # show full metadata
            # Call the class method directly to open the file
            item.open()
        else:
            print("Going back to menu.")



def menu():
    library = initial_library
    access = get_valid_access()  # Ask once at the start

    while True:
        print("1. View all files (metadata only)")
        print("2. Search by title")
        print("3. Search by genre")
        print("4. Open a file")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_library_metadata(library)
            show_full_file(library)  # Ask user if they want full details
        elif choice == "2":
            search_by_title(library, access)
        elif choice == "3":
            search_by_genre(library, access)
        elif choice =="4":
            display_library_metadata(library)
            num = input("Enter file number to open: ")

            if num.isdigit():
               num = int(num)
            if 1 <= num <= len(library):
                    library[num - 1].open()   # ⭐ THIS LINE MATTERS
            else:
              print("Invalid number")

        elif choice == "5":
            print("👋 Thank you for using the Digital Library!")
            break
        else:
            print("⚠️ Invalid choice. Please select 1–4.")




def get_valid_access():
    while True:
        access = input("Enter access type (user/admin): ").strip().lower()
        if access in ["user", "admin"]:
            return access
        print("Invalid access type. Please enter 'user' or 'admin'.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


menu()



