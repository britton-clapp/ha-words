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
        const stateStr = state ? state.state : 'unavailable';
        const header = this.config.title || "";
        const main_word = this.config.show_word ? `<p class="words-main-word">${stateStr}</p>` : "";
        const part_of_speech = this.config.show_part_of_speech ? `<p class="words-part-of-speech"><em>${state.attributes.part_of_speech.trim()}</em></p>` : "";
        const example = this.config.show_example ? `<p class="words-example">&quot;${state.attributes.example.trim()}&quot;</p>` : "";
        const separator = this.config.show_example && this.config.show_definition ? "<hr>" : "";
        const definition = this.config.show_definition ? `<p class="words-definition">${state.attributes.definition.trim()}</p>` : "";
        const always_light_background = this.config.always_light_background ? "background-color: #fcfbf7;" : "";

        // done once
        if (!this.content) {
            this.innerHTML = `
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Old+Standard+TT:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
            <style>
            .words-card {
                font-family: "Old Standard TT", "Times New Roman", serif;
                font-weight: 400;
                font-style: normal;
            }
            .words-card-container {
                padding: 1.5rem;
                ${always_light_background}
            }
            .words-main-word {
                font-size: 2rem;
                font-weight: 600;
                margin-bottom: 0;
                margin-top: 0.5rem;
            }
            .words-part-of-speech {
                margin-top: 0.5rem;
            }
            .words-definition {
                font-size: 1.5rem;
            }
            .words-example {
                color: #666;
                font-style: italic;
            }
            </style>
            <ha-card class="words-card-container" header="${header}">
                <div class="card-content words-card"></div>
            </ha-card>
            `;
            this.content = this.querySelector('div');
        }
        this.content.innerHTML = `
            ${main_word}
            ${part_of_speech}
            ${definition}
            ${separator}
            ${example}
        `;
    }
}

customElements.define('random-word-card', RandomWordCard);