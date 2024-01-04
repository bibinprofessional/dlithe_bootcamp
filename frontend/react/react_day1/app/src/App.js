
import './App.css';
import Navbar from './Components/Navbar';
import Greet from './Components/Greet';
import GreetClass from './Components/GreetClass';
import Count from './Components/Count';
import Message from './Components/Message';
import CountFunction from './Components/CountFunction';
import Footer from './Components/Footer';
import ReverseCounter from './Components/ReverseCounter';
import Square from './Components/Square';
import Condition from './Components/Condition';
import CheckPositive from './Components/CheckPositive';
import CheckEven from './Components/CheckEven';
import MyList from './Components/MyList';
import ExampleForLifeCycle from './Components/ExampleForLifeCycle';
import CountDownTimer from './Components/CountDownTimer';
import Style from './Components/Style';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Greet name='bibin' age='23' />
      <Greet name='srujan' age='23' />
      <GreetClass age='20' />
      <Count />
      <Message />
      <CountFunction />
      <ReverseCounter />
      <Square />
      <Footer />
      <Condition logged="1" name="admin" />
      <CheckEven number='10' />
      <CheckPositive number='-11' />
      <MyList />
      <ExampleForLifeCycle />
      <CountDownTimer />
      <Style primary="false" />



    </div>
  );
}

export default App;
