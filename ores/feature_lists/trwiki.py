from revscoring.features import (diff, page, parent_revision,
                                 revision, user)
from revscoring.features.modifiers import log

from . import generic

damaging = [
    log(diff.added_symbolic_chars_ratio + 1),
    log(diff.chars_added + 1),
    log(diff.chars_removed + 1),
    diff.longest_repeated_char_added,
    diff.longest_token_added,
    log(diff.markup_chars_added + 1),
    log(diff.markup_chars_removed + 1),
    log(diff.numeric_chars_added + 1),
    log(diff.numeric_chars_removed + 1),
    diff.proportion_of_chars_added,
    diff.proportion_of_chars_removed,
    diff.proportion_of_markup_chars_added,
    diff.proportion_of_numeric_chars_added,
    diff.proportion_of_symbolic_chars_added,
    diff.proportion_of_uppercase_chars_added,
    log(diff.segments_added + 1),
    log(diff.segments_removed + 1),
    log(diff.symbolic_chars_added + 1),
    log(diff.symbolic_chars_removed + 1),
    log(diff.uppercase_chars_added + 1),
    log(diff.uppercase_chars_removed + 1),
    log(diff.words_added + 1),
    log(diff.words_removed + 1),
    diff.bytes_changed + 1,
    diff.bytes_changed_ratio,
    page.is_content_namespace,
    parent_revision.was_same_user,
    log(parent_revision.words + 1),
    log(user.age + 1),
    user.is_anon,
    user.is_bot,
    log(diff.added_badwords_ratio + 1),
    log(diff.badwords_added + 1),
    log(diff.badwords_removed + 1),
    diff.proportion_of_badwords_added,
    diff.proportion_of_badwords_removed
]

good_faith = generic.good_faith + [
    log(diff.added_badwords_ratio + 1),
    log(diff.badwords_added + 1),
    log(diff.badwords_removed + 1),
    log(diff.proportion_of_badwords_added + 1),
    log(diff.proportion_of_badwords_removed + 1),
    log(diff.removed_badwords_ratio + 1),
    log(parent_revision.badwords + 1),
    log(parent_revision.proportion_of_badwords + 1),
    log(revision.badwords + 1),
    log(revision.proportion_of_badwords + 1)
]
