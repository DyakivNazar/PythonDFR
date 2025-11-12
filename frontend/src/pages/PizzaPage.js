import {PizzaForm} from "../components/PizzaForm";
import {Chat} from "../components/Chat";
import {PizzasComp} from "../components/PizzasComp";

const PizzaPage = () => {
    return (
        <div>
            <PizzaForm/>
            <hr/>
            <PizzasComp/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {PizzaPage};