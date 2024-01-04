import React, { Component } from 'react'

export class CountDownTimer extends Component {
    constructor(props) {
        super(props)

        this.state = {
            count: 10,
        }


    }
    componentDidMount() {
        this.myInterval = setInterval(() => {
            const count = this.state.count
            if (count > 0) {
                this.setState({
                    count: count - 1
                })
            }
            if (count == 0) {
                clearInterval(this.myInterval)
            }
        }, 1000);
    }
    componentWillUnmount() {
        clearInterval(this.myInterval)


    }
    render() {
        const count = this.state.count
        return (
            <div>
                <h2 style={{ backgroundColor: 'green' }}>counter:{count}</h2>
            </div>
        )
    }
}

export default CountDownTimer