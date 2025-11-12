import {useEffect, useState} from "react";
import {pizzaService} from "../services/pizza.service";
import {socketService} from "../services/socket.service";
import {PizzaComp} from "./PizzaComp";

const PizzasComp = () => {
    const [pizzas, setPizzas] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        pizzaService.getAll({ order: '-id' }).then(({data}) => setPizzas(data.data))
    }, [trigger]);

    useEffect(() => {
        socketInit().then()
    }, []);

    const socketInit = async () => {
        const {pizzas} = await socketService();
        const client = await pizzas();

        client.onopen = () => {
            console.log('Pizza socket connected');
            client.send(JSON.stringify({
                action: 'subscribe_to_pizza_model_changes',
                request_id: new Date().getTime()
            }))
        }

        client.onmessage = ({data}) => {
            console.log(data);
            setTrigger(prev => !prev)
        }
    }
    return (
        <div>
            {pizzas.map(pizza => <PizzaComp key={pizza.id} pizza={pizza}/>)}
        </div>
    );
};

export {PizzasComp};