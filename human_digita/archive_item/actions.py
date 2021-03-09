from human_digita.archive_item.models import ArchiveItem


def check_duplicate_archive_item(new_archive_item: ArchiveItem):
    try:
        old_archive_items = ArchiveItem.objects.filter(modified_date=new_archive_item.modified_date)
        if old_archive_items.exists():
            return old_archive_items[0]
        else:
            raise
    except:
        return False
