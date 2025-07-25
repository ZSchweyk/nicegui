import weakref
from typing import TYPE_CHECKING, Generic, List, Optional, TypeVar

if TYPE_CHECKING:
    from .element import Element

T = TypeVar('T', bound='Element')


class Classes(list, Generic[T]):

    def __init__(self, *args, element: T, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._element = weakref.ref(element)

    @property
    def element(self) -> T:
        """The element this classes object belongs to."""
        element = self._element()
        if element is None:
            raise RuntimeError('The element this classes object belongs to has been deleted.')
        return element

    def __call__(self,
                 add: Optional[str] = None, *,
                 remove: Optional[str] = None,
                 toggle: Optional[str] = None,
                 replace: Optional[str] = None) -> T:
        """Apply, remove, toggle, or replace HTML classes.

        This allows modifying the look of the element or its layout using `Tailwind <https://v3.tailwindcss.com/>`_ or `Quasar <https://quasar.dev/>`_ classes.

        Removing or replacing classes can be helpful if predefined classes are not desired.

        :param add: whitespace-delimited string of classes
        :param remove: whitespace-delimited string of classes to remove from the element
        :param toggle: whitespace-delimited string of classes to toggle (*added in version 2.7.0*)
        :param replace: whitespace-delimited string of classes to use instead of existing ones
        """
        # DEPRECATED: replace Tailwind v3 link with v4 (throughout the whole codebase!) after upgrading in NiceGUI 3.0
        element = self.element
        new_classes = self.update_list(self, add, remove, toggle, replace)
        if self != new_classes:
            self[:] = new_classes
            element.update()
        return element

    @staticmethod
    def update_list(classes: List[str],
                    add: Optional[str] = None,
                    remove: Optional[str] = None,
                    toggle: Optional[str] = None,
                    replace: Optional[str] = None) -> List[str]:
        """Update a list of classes."""
        class_list = classes if replace is None else []
        class_list = [c for c in class_list if c not in (remove or '').split()]
        class_list += (add or '').split()
        class_list += (replace or '').split()
        class_list = list(dict.fromkeys(class_list))  # NOTE: remove duplicates while preserving order
        if toggle is not None:
            for class_ in toggle.split():
                if class_ in class_list:
                    class_list.remove(class_)
                else:
                    class_list.append(class_)
        return class_list
