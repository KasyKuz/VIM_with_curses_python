from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов. Он также
    хранит ссылку на экземпляр подкласса Состояния, который отображает текущее
    состояние Контекста.
    """

    _state = None
    """
    Ссылка на текущее состояние Контекста.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        Контекст позволяет изменять объект Состояния во время выполнения.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    Контекст делегирует часть своего поведения текущему объекту Состояния.
    """

    def request1(self):
        self._state.Controller_work()

    def request2(self):
        self._state.View_work()

    def request3(self):
        self._state.Model_work()


class State (ABC):
    """
    Базовый класс Состояния объявляет методы, которые должны реализовать все
    Конкретные Состояния, а также предоставляет обратную ссылку на объект
    Контекст, связанный с Состоянием. Эта обратная ссылка может использоваться
    Состояниями для передачи Контекста другому Состоянию.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def Mode0(self) -> None:
        pass

    @abstractmethod
    def Mode1(self) -> None:
        pass

    @abstractmethod
    def Mode2(self) -> None:
        pass
    @abstractmethod
    def Mode3(self) -> None:
        pass

class Help_state(State):
    def __init__(self, controller, view, model):
        self.controller = controller
        self.view = view
        self.model = model

    def Controller_work(self) -> None:
        pass
    
    def View_work(self) -> None:
        pass
   
    def Model_work(self) -> None:
        pass


class Text_state(State):
    def __init__(self, controller, view, model):
        self.controller = controller
        self.view = view
        self.model = model

    def Controller_work(self) -> None:
        self.controller.start()

    
    def View_work(self) -> None:
        pass
   
    def Model_work(self) -> None:
        pass
    

class Command_state(State):
    def __init__(self, controller,view,model):
        self.controller = controller
        self.view = view
        self.model = model
    def Controller_work(self) -> None:
        self.controller.start()