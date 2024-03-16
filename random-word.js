class RandomWordCard extends HTMLElement {

    config;
    content;

    // required
    setConfig(config) {
        this.config = config;
    }

    set hass(hass) {
        const entityId = this.config.entity;
        const state = hass.states[entityId];
        console.log('state', state);
        const stateStr = state ? state.state : 'unavailable';

        // done once
        if (!this.content) {
            // user makes sense here as every login gets it's own instance
            this.innerHTML = `
                <ha-card header="Random word">
                    <div class="card-content"></div>
                </ha-card>
            `;
            this.content = this.querySelector('div');
        }
        // done repeatedly
        this.content.innerHTML = `
            <p><em>${stateStr}</em></p>
            <p>&quot;${state.attributes.definition}&quot;</p>
        `;
    }
}

customElements.define('random-word-card', RandomWordCard);