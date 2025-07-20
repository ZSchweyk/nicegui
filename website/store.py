from nicegui import ui
from collections import defaultdict

from .style import example_link, features, heading, link_target, section_heading, subtitle, title


ui.add_head_html('<link href="https://cdn.jsdelivr.net/themify-icons/0.1.2/css/themify-icons.css" rel="stylesheet" />')


# --- Audio data ---
AUDIO_FILES = [
    {
        "name": "Song 1",
        "id": "s1",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 50,
        "category": "Improv"
    },
    {
        "name": "Song 2",
        "id": "s2",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 299,
        "category": "Improv"
    },
    {
        "name": "Song 3",
        "id": "s3",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 199,
        "category": "Covers"
    },
    {
        "name": "Song 4",
        "id": "s4",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 299,
        "category": "Covers"
    },
    {
        "name": "Song 5",
        "id": "s5",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 199,
        "category": "Originals"
    },
    {
        "name": "Song 6",
        "id": "s6",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 299,
        "category": "Originals"
    },
    {
        "name": "Song 7",
        "id": "s7",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 199,
        "category": "Originals"
    },
    {
        "name": "Song 8",
        "id": "s8",
        "preview": "previews/s1_preview.mp3",
        "full": "static/music/tracks/s1.mp3",
        "price_cents": 299,
        "category": "Originals"
    },
]

checkboxes = {}

def tracks_tab_contents():
    # --- Group tracks by category ---
    categories = defaultdict(list)
    for track in AUDIO_FILES:
        categories[track['category']].append(track)
    for category, tracks in categories.items():
        with ui.expansion(
            category,
            caption="Caption",
            group="",
            # value=category=="Originals"
            ).classes("w-full"):
            with ui.column().classes("w-full gap-4"):
                for track in tracks:
                    track_id = track['id']
                    with ui.card().classes("w-full no-shadow"):
                        with ui.column().classes("w-full gap-1"):
                            # On small screens: stacked; on md+ screens: horizontal row
                            with ui.row().classes("flex flex-col md:flex-row md:justify-between md:items-center md:w-3/4 gap-2"):
                                checkboxes[track_id] = ui.checkbox(track['name']).on_value_change(lambda e: 1)
                                # ui.label(track['name']).classes('text-xl font-semibold')
                                ui.audio(track["full"], controls=True).props("controlsList='nodownload'")
                                ui.label(f"${track['price_cents'] / 100:.2f}").classes('text-lg')
                            # On small screens: stacked; on md+ screens: horizontal row
                            # with ui.row().classes("flex flex-col md:flex-row md:justify-between md:items-center w-full gap-2"):
                                # ui.label(f"${track['price_cents'] / 100:.2f}").classes('text-lg')
                                # checkboxes[track_id] = ui.checkbox('Select').on_value_change(lambda e: 1)
                    
                    
                    
                    
                    
                    # My original layout
                    # with ui.card().classes("w-full no-shadow"):
                    #     with ui.row().classes('justify-between items-center w-full mt-2'):
                    #         ui.label(track['name']).classes('text-xl font-semibold')
                    #         ui.audio(track["full"], controls=True).classes('mt-2')  # no w-full if you want this on the same row as the label
                    #         ui.label(f"${track['price_cents'] / 100:.2f}").classes('text-lg')
                    #         checkboxes[track_id] = ui.checkbox('Select').on_value_change(lambda e: 1)



def render_store_ui():
    with ui.row().classes('''
            dark-box min-h-screen no-wrap
            justify-center items-center flex-col md:flex-row
            py-10 px-8 lg:px-16
            gap-8 sm:gap-16 md:gap-8 lg:gap-16
        '''):
        link_target('store')
        with ui.column().classes('w-full text-white max-w-4x1'):
            # heading('Store')
            # ui.label("Select tracks/albums")
            with ui.column().classes('w-full gap-2 bold-links arrow-links text-lg'):
                with ui.row().classes("w-full flex-row justify-between"):
                    with ui.tabs().classes("") as tabs:
                        ui.tab('t', label='Tracks')
                        ui.tab('a', label='Albums')
                    ui.button("Checkout")
                
                # with ui.scroll_area().classes("w-full h-96"):
                with ui.tab_panels(tabs, value='t').classes('w-full'):
                    with ui.tab_panel('t'):
                        tracks_tab_contents()
                    with ui.tab_panel('a'):
                        ui.label('Albums')
