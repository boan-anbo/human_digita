from human_digita.archive.const import ArchiveTypes
from human_digita.archive_item.actions import check_duplicate_archive_item
from human_digita.archive_item.const import ArchiveItemKeyTypes
from human_digita.archive_item.models import ArchiveItem
from human_digita.document.const import DocumentType
from human_digita.document.models import Document

# return false is there is no duplicate, return the existing document if there is not
def check_duplicate_document(new_doc):
    try:
        old_docs = Document.objects.filter(title=new_doc.title, pages=new_doc.pages)
        if old_docs.exists():
            return old_docs[0]
        else:
            raise
    except:
        return False

def save_doc_info_to_document(docInfo, update=True) -> Document:
    try:
        creator = docInfo.get('creator', None)

        author_string = docInfo.get('author', None)
        modified_date = docInfo.get('modifiedDate', None)
        created_date = docInfo.get('createdDate', None)

        file_name = docInfo['fileName']
        file_path = docInfo.get('filePath', None)
        cite_key = docInfo.get('citeKey', None)
        pages = docInfo.get('pages', None)

        new_doc = Document()
        new_doc.title = file_name
        new_doc.pages = pages
        new_doc.author_string = author_string

        old_doc = check_duplicate_document(new_doc)
        if old_doc == False:
            new_doc.save()
        else:
            new_doc = old_doc

        new_archive_item = ArchiveItem()
        new_archive_item.title = file_name
        new_archive_item.file_name = file_name
        new_archive_item.file_path = file_path
        new_archive_item.modified_date = modified_date
        new_archive_item.created_date = created_date
        if cite_key:
            new_archive_item.key = cite_key
            new_archive_item.key_type = ArchiveItemKeyTypes.CITE_KEY
        old_archive_item = check_duplicate_archive_item(new_archive_item)
        if not old_archive_item:
            new_archive_item.save()
        else:
            new_archive_item = old_archive_item
        # if there is archive item and there is no old odoc
        if new_archive_item and old_doc == False:
            new_doc.archive_item = new_archive_item
            new_doc.save()
            # if there is arachi item and old doc(which is reassinged as the new doc) has no archive item and the option is set to update
        if new_archive_item and old_doc and update:
            new_doc.archive_item = new_archive_item
            new_doc.save()

        return new_doc


    except Exception as e:
        print(e)
        raise
